import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localhost_ip = socket.gethostbyname(local_hostname)

sever_address = (localhost_ip, 50007)
sock.connect(sever_address)


#temperature_data = ["am", "you", "are", "have"]
#for entry in temperature_data:
    #print("data: %s" %entry)
f = open("in-proj0.txt")
lines = f.readlines()
for line in lines:
    new_data = str("%s" % line).encode("utf-8")
    sock.sendall(new_data)

    time.sleep(2)

    data_from_server=sock.recv(100)
    print("final data received:{}".format(data_from_server.decode('utf-8')))


sock.close()