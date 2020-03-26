import socket
mysoc=socket.socket()
mysoc.connect(('data.pr4e.com',80))

cmd='GET https://www.py4e.com/romeo.txt HTTP/1.0\n\n'.encode()
mysoc.send(cmd)

while True:
    data=mysoc.recv(512)
    if(len(data)>1):
        print(data.decode())
    else:
        break
mysoc.close()