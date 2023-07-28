import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("PC Name:" +hostname)
print("ip" +ip)