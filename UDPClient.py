import socket

IP = "127.0.0.1"
port = 44444


UDPClientsocket = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)

while True:
    message = input(">")
    sendthis = str.encode(message)

    UDPClientsocket.sendto(sendthis, (IP,port))
    data,addr = UDPClientsocket.recvfrom(1024)

    print("msg from server is:" + str(data))
    UDPClientsocket.close()
    