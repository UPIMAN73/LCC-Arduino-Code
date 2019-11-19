from client_class import Client
from server_class import Server
from threading import Thread


if __name__== "__main__":
    c = None
    s = None
    try:
        client_port = 9001 # this is the other server's port
        server_port = 9001 # this is the port that you are hosting

        ## Server Setup
        s = Server("", server_port)
        s.bindSetup()
        x = Thread(target=s.serverLoop)
        x.start()
        

        ## Client Setup
        c = Client("", client_port)
        c.connect()
        y = Thread(target=c.clientLoop)
        y.start()

        x.join()
        y.join()
    
    except KeyboardInterrupt:
        print("Pressed CTL+C")

    finally:
        if s:
            s.close()
        if c:
            c.close()
