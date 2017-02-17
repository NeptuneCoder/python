import socket

target_host = "www.baidu.com"

target_post = 80

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto("AAAABBBBCCCC",(target_host,target_post))

daata,addr = client.recvfrom(2096)
print "-----------"
print data
print "-----------"