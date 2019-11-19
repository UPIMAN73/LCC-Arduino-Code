from server_class import Server
from threading import Thread, ThreadError

class ServerThread(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.s = Server()