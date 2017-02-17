import socket

target_post = 80
target_host = "www.baidu.com"

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


client.sendto("4999999",(target_host,target_post))

data,addr = client.recvfrom(4096)

print data