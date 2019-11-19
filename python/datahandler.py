from datetime import datetime
from packet import Packet

class DataHandler:
    def __init__(self):
        self.packetList = []
    
    def packetExists(self, packet):
        if packet in self.packetList:
            return True
        return False
    
    def addPacket(self, packet):
        self.packetList.append(packet)
    
    def sort(self):
        tempArray = self.packetList
        for i in range(0, len(self.packetList)):
            for j in range(0, len(self.packetList)):
                if (tempArray[i].size < tempArray[j].size):
                    temp = tempArray[i]
                    tempArray[i] = tempArray[j]
                    tempArray[j] = temp
        self.packetList = tempArray
    
    # Minimum size of the packet list packets
    def minSize(self):
        min_val = self.packetList[0].size
        for i in self.packetList:
            if min_val >= i.size:
                continue 
            if min_val > i.size:
                min_val = i.size
        return min_val
    
    # maximum packet size within packet list
    def maxSize(self):
        max_val = self.packetList[0].size
        for i in self.packetList:
            if max_val >= i.size:
                continue
            if max_val < i.size:
                max_val = i.size
        return max_val
    

    # Write all packet information to a file
    def write(self, fname):
        f = open(fname, "w")
        for i in self.packetList:
            f.write(str(i.header) + "_" + str(i.size) + "_" + str(i.msg) + "\n")
        f.close()





# d = DataHandler()

# d.packetList = [Packet("DAT", 9, "INF"), Packet("DAT", 7, "POOP"), Packet("DAT", 2, "IN"), Packet("DAT", 1, "N"), Packet("DAT", 10, "Hello World!")]
# for i in d.packetList:
#     print(i.size)

# print()
# d.sort()
# for i in d.packetList:
#     print(i.size)
