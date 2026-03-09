import socket

s = socket.socket()
s.connect(('localhost', 8001))

while True:
    mac = input("Enter Physical Address (MAC): ")
    s.send(mac.encode())
    print("IP Address:", s.recv(1024).decode())