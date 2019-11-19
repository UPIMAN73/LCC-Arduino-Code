from packet import Packet
from threading import Thread
from datahandler import DataHandler
from datetime import datetime
import socket


class Server:
    def __init__(self, addr, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        self.port = port
        self.bind = False
        self.connection_list = []
        self.threadList = []
        self.dataList = DataHandler()
    
    # use this function to connect to the server
    def bindSetup(self):
        try:
            self.socket.bind((self.addr, self.port))
            print("Succesful Setup for %s on port %d" % (self.addr, self.port))
            self.bind = True
        except socket.error as err:
            print("Socket setup failure... Cannot host the server %s on port %d" % (self.addr, self.port))
            print(err)
    

    """
    The "Server" or Read loop from the Client
    """

    # server loop for the program
    def serverLoop(self):
        conn = None
        bconn = False
        self.socket.listen(0)
        while (self.bind):
            try:
                # setting up the connection and accepting it
                conn = None
                conn, addr = self.socket.accept()
                print("SERVER >> Connection Established with %s" % (str(addr)))
                bconn = True

                # new thread process
                x = Thread(target=self.readLoop, args=(conn, addr))
                x.start()
                self.connection_list.append(conn)
                print("SERVER >> Connection List: %s" % (self.connection_list))
                x.join()
                
            
            # connection setup
            except socket.error as error:
                print("\nSERVER >> ERROR: Server Socket Failure Accepting Client")
                print(error)
                bconn = False
            
            except KeyboardInterrupt:
                print("\nSERVER >> Pressed CTL+C")
                self.bind = False
                self.close()
                break
            
            # close the connection
            finally:
                if (conn != None or bconn == True):
                    conn.close()

    # Setup the read loop
    def readLoop(self, conn, adr):
        try:
            """
            Data variables for manipulating packets and handling them
            """
            data = Packet("", 0, "")
            sdata = ""
            connection = True

            while (connection):
                # if the user quits
                if (data.msg.lower() == "quit" or not connection):
                    connection = False
                    break
                # else send the message
                else:                  
                    sdata = conn.recv(256).decode()
                    data.packetReformatString(sdata)
                    print("\nSERVER >> Recieving Data >> %s >> %s\t%d\t%s" % (adr, data.header, data.size, data.msg))
                    if (data.header == "MSG" or data.header == "DAT"):
                        self.dataList.addPacket(Packet(data.header, data.size, data.msg))
        
        except socket.error as err:
            print("SERVER >> Broken connection with %s on port %d" % (self.addr, self.port))
            print(err)
        
        finally:
            self.dataList.write(str(datetime.now()) + ".txt")
            self.connection = False
            conn.close()
            self.connection_list.remove(conn)
            print("Connection List: %s" % (self.connection_list))
    

    def close(self):
        print("SERVER >> Closing Socket on server %s on port %d..." % (self.addr, self.port))
        self.socket.close()
        print("SERVER >> Socket Closed")
        print("SERVER >> Clearing Connection List")
        self.connection_list = None