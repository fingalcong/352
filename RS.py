import socket
TSHostname = ''
rsListenPort = 50009
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localhost_ip = socket.gethostbyname(local_hostname)

print("working on %s with %s" % (local_hostname, localhost_ip))

sever_address = ('', rsListenPort)
sock.bind(sever_address)

sock.listen(1)

f = open("PROJI-DNSRS.txt")
list = f.readlines()
#for i in range(len(list)):
all = []

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
            list = []
            list.append(data)
            #print(list)
            #print (data)
            new = data.strip('\n').lower()
            if new in dict:
                    #all.append(dd[new])
                    connection.sendall(bytes(dd[new], 'utf-8'))
                    #break
            else:
                    error = new + ' - NS'
                    #all.append(error)
                    connection.sendall(bytes(error, 'utf-8'))
                    all.append(new)
                    #print(all)
                #if i == len(list):
                    #error = new + ' - NS'
                    #connection.sendall(bytes(error, 'utf-8'))

            if data:
                print ("data received: %s" %data)
            else:
                #print("done")
                break
        #del all[3]
        #print(all)
    finally:
        connection.close()