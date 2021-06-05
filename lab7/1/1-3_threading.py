import socket
import threading
import json
import time

class Server:
    def __init__(self, IP, Port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((IP, Port))
        self.s.listen(1)
        print("Server running...")

        while True:
            c, a = self.s.accept()
            sThread = threading.Thread(target=self.handler, args=(c, a))
            sThread.start()
            print(str(a[0]) + ': ' + str(a[1]) + ' connected')

    def handler(self, c, a):
        try:
            data = c.recv(1024)
            if data:
                msg = data.decode("utf-8")
                mag= str(msg)
                try:
                    with open("Server/" + msg, 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            c.sendall(line.encode('utf-8'))
                except:
                    print("There is no such file!")
                    c.send("Failed!".encode('utf-8'))

        except:
            print(str(a[0]) + ':' + str(a[1]) + 'disconnected')

    def shotdown(self):
        self.s.close()



class Client:
    def __init__(self, IP, Port, my_ID):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        (self.s).connect((IP, Port))
        print(my_ID + " Connected to the server")
        self.Id= my_ID

    def SendMessage(self, sock, message):
        #print("Client " + self.Id + " sent " + str(message))
        data = sock.send(bytes(message, 'utf-8'))

    def getinput(self, message):
        cThread = threading.Thread(target=self.SendMessage, args=(self.s, message,))
        cThread.daemon = True
        cThread.start()

        with open("client" + self.Id+ "_" + message, 'w') as file:
            data = self.s.recv(1024)
            file.write(data.decode('utf-8'))

    def shotdown(self):
        self.s.close()


def make_Server():
    self.server = Server("127.0.0.1", 4000)

sThread = threading.Thread(target= make_Server, args=())
sThread.start()

n= int(input("How many clients do you want?\n"))
clients= []

for i in range(n):
    client= Client("127.0.0.1", 4000, str(i))
    clients.append(client)

time.sleep(0.1)

for i in range(n):
    filename= input("which file does client "+  str(i) + " need?\n")
    clients[i].getinput(filename)
