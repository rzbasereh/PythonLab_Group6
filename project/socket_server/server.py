import socket
import os

# making a list from Volume folder
image_names = []
for name in os.listdir('./Volume'):
    image_names.append(name)

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# for the error : address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# associate the socket with a port
host = '127.0.0.1' # can leave this blank on the server side
port = 2000
s.bind((host, port))

# accept "call" from client
s.listen()
conn, addr = s.accept()
print('client is at : ',addr)

# getting data
data = conn.recv(100000).decode()
# for splitting dict data , if you have send : data = {"name":"20.jpg"} , you will get : name = 20.jpg
name = data.split("{")[1].split(": ")[1].replace('"}','').replace('"','')

# searching in folder Volume
if name in image_names:
    print("there is this image")
    with open("./Volume/"+name, 'rb') as img:
        img_byte = img.read()
    # sending the image to the client in byte format
    conn.sendall(b'HTTP/1.1 200 ok\r\nContent-Type: image/jpeg\r\nTransfer-Encoding: chunkedcontent\r\n\r\n' + img_byte)

else:
    print("there is not this image")
    out_text = b"there is not this image"
    # sending the error text to the client
    conn.sendall(b'HTTP/1.1 200 ok\r\nContent-Type: text/plain\r\nTransfer-Encoding: chunkedcontent\r\n\r\n' + out_text)

# close the connection
conn.close()