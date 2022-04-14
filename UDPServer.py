import socket

IP = "127.0.0.1"
port = 44444


UDPServersocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServersocket.bind((IP, port))

print("server is listening")

while True:
    data, addr = UDPServersocket.recvfrom(1024)
    print(str(data))
    response = "Received msg is: " + data.decode('utf-8')
    UDPServersocket.sendto(str.encode(response),addr)
