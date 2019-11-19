import socket
from packet import Packet

class Client:
    def __init__(self, addr, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        self.port = port
        self.connection = False
    
    # use this function to connect to the server
    def connect(self):
        try:
            self.socket.connect((self.addr, self.port))
            print("CLIENT >> Succesful connection to %s on port %d" % (self.addr, self.port))
            self.connection = True
        except socket.error as err:
            print("CLIENT >> Socket connection failure... Cannot connect to the server %s on port %d" % (self.addr, self.port))
            print(err)
    


    """
    The "client" or write loop to the server
    """

    # Setup the send loop
    def clientLoop(self):
        try:
            """
            Data variables for manipulating packets and handling them
            """
            data = Packet("", 0, "")
            hdata = ""
            mdata = ""

            while (self.connection):
                # if the user quits
                if (mdata.lower() == "quit" or data.msg.lower() == "quit"):
                    self.connection = False
                    self.close()
                    break
                # else send the message
                else:
                    hdata = str(input("Header (CMD, MSG, DAT): ")).upper()
                    while (not data.checkHeader(hdata)):
                        print("\n\nCLIENT >> Can only have MSG, CMD, or DAT type packets")
                        hdata = str(input("Header (CMD, MSG, DAT): "))
                    
                    mdata = str(input("Message: "))
                    while (not data.checkMessage(mdata)):
                        print("CLIENT >> Message must be less than 256 characters (bytes)")
                        mdata = str(input("Message: "))
                    
                    data.packetReformat(hdata, mdata)
                    self.send(data.packetFormat())
                    print("CLIENT >> Sending Data >> %s\t%d\t%s" % (data.header, data.size, data.msg))
        
        except socket.error as err:
            print("CLIENT >> Broken connection with %s on port %d" % (self.addr, self.port))
            print(err)
        
        finally:
            self.connection = False
            self.close()


    # Send a packet to the server
    def send(self, packet):
        try:
            if self.connection == True:
                self.socket.send(bytes(packet, "utf-8"))
        except socket.error as err:
            print("CLIENT >> Cannot send packet to server %s on port %d" % (self.addr, self.port))
            print(err)
            self.connection = False
            self.close()
    

    def close(self):
        if self.socket != None:
            print("CLIENT >> Closing Socket on server %s on port %d..." % (self.addr, self.port))
            self.socket.close()
            print("CLIENT >> Socket Closed")
            self.socket = None
        else:
            print("CLIENT >> This socket is already closed")
