import socket
TSHostname = ''
tsListenPort = 50010

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localhost_ip = socket.gethostbyname(local_hostname)

print("working on %s with %s" % (local_hostname, localhost_ip))

sever_address = ('', tsListenPort)
sock.bind(sever_address)

sock.listen(1)

f = open("PROJI-DNSTS.txt")
list = f.readlines()
#for i in range(len(list)):
dict = set()
dd = {}
for item in list:
    s = item.split()
    dict.add(s[0].strip('\n'))
    hostname = s[0].strip('\n')
    dd[hostname] = item
while True:
    print ("wait for a connection")
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(100).decode()
            new = data.strip('\n')
            if new in dict:
                    connection.sendall(bytes(dd[new], 'utf-8'))
                    #break
            else:
                    error = new + ' - Error:HOST NOT FOUND'
                    connection.sendall(bytes(error, 'utf-8'))
                #if i == len(list):
                    #error = new + ' - NS'
                    #connection.sendall(bytes(error, 'utf-8'))

            if data:
                print ("data received: %s" %data)
            else:
                print("done")
                break
    finally:
        connection.close()