import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print("ARP Server is listening on port 8000...")
c, addr = s.accept()

address = {
    "148.129.123.45": "5D:BC:E3:FA",
    "109.178.123.45": "8A:2B:3C:4D",
}

while True:
    ip = c.recv(1024).decode()
    print(f"Received IP: {ip}")
    mac = address.get(ip, "Not Found")
    c.send(mac.encode())