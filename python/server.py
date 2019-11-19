import socket
from packet import Packet

# Port and Address Setup
addr = ""
port = 9002

try:
    # Socket Setup
    s = socket.socket()
    print("Socket is setup")

    s.bind((addr, port))
    # Issue with printing format
    print("Succesfully setup server bind on port %d" % (port))

    print("Waiting for a connection...")
    s.listen(5)
    client, addr = s.accept()

    # Issue with printing format
    print("Recieved a connection with address %s" % (str(addr)))

    # Data variables
    data = Packet("", 0, "")
    sdata = ""
    quit_mode = False

    # while loop for incoming data
    while (not quit_mode):
        # if the incoming data is to quit then quit
        if (sdata == None or data.msg == "quit"):
            quit_mode = True
            break
        else:
            sdata = client.recv(256).decode()
            print(sdata)
            print(data.packetReformatString(sdata))

            # ISSUE With printout format
            print("Client Data >> %s\t%d\t%s" % (data.header, data.size, data.msg))

except socket.error as err:
    print(err)

finally:
    # Closing Socket
    print("Socket closing")
    client.close()
    s.close()
    print("Socket closed")