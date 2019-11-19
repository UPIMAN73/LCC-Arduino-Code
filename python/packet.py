class Packet:
    def __init__(self, header, size, msg):
        """
            Message packet - MSG
            Data packet - DAT
            CMD Packet - CMD

            Timestamp will be added to othe msg part of the packet like so
            TYPE_SIZE_|TIMESTAMP|MSG
            Timestamps are always 26 letters/bytes
        """
        self.header = header
        
        # Same with message
        if (len(msg) < 257):
            self.msg = msg
        else:
            self.msg = ""
        
        self.size = len(self.msg)
    
    # print out the packet format
    def packetFormat(self):
        return str(self.header) + "_" + str(self.size) + "_" + str(self.msg)
    
    # Reformat the packet from a given string
    def packetReformatString(self, s):
        p = s.split("_")
        if (len(p) == 3):
            self.header = p[0]
            self.size = int(p[1])
            self.msg = p[2]
            return [self.header, self.size, self.msg]
        else:
            return ["CMD", 4, "quit"]
    
    # reformat the packet information
    def packetReformat(self, header, message):
        if (self.checkHeader(header)):
            if (self.checkMessage(message)):
                self.setHeader(header)
                self.setMessage(message)
                self.size = len(self.msg)
            else:
                print("Failed Message")
                print(message)
    
    """
    Setting and checking valid headers and message data
    """
    def setHeader(self, header):
        if self.checkHeader(header):
            self.header = header
        else:
            print("ERROR: Cannot have that type as a header, it is unrecognizable")
    

    def setMessage(self, message):
        if self.checkMessage(message):
            self.msg = message
        else:
            print("ERROR: Cannot have data be more than 256 characters (bytes)")
    

    def checkHeader(self, header):
        if header == "MSG" or header == "CMD" or header == "DAT" or header == "TST":
            return True
        else:
            return False
    

    def checkMessage(self, message):
        if (len(message) < 257):
            return True
        else:
            return False