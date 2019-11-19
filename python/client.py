import socket
from packet import Packet

# address and port connection
addr = ""
port = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
print("Connecting to server...")
try:
    s.connect((addr, port))
except socket.error as err:
    print("Cannot connect to server %s on port %d", (addr, port))
    print(err)

print("Successfully connected to server %s on port %d", (addr, port))


# Setting up data and packet items
data = Packet("", 0, "")
hdata = ""
msize = 0
mdata = ""
sdata = ""
quit_mode = False

while (not quit_mode):
    # if the incoming data is to quit then quit
    if (mdata == "quit" or data.msg == "quit"):
        quit_mode = True
        break
    else:
        print("Please write out the header first before writing the message.")
        hdata = str(input("Header (MSG, CMD, DAT): "))
        mdata = str(input("Message: "))
        msize = len(mdata)
        sdata = hdata + "_" + str(msize) + "_" + mdata
        s.send(bytes(sdata, "utf-8"))
        
        # print out information
        print(data.packetReformat(sdata))
        print("Client Data >> %s\t%d\t%s", (data.header, data.size, data.msg))


# Closing Socket
print("Socket closing")
s.close()
print("Socket closed")