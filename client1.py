import socket

results=[]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localhost_ip = socket.gethostbyname(local_hostname)

sever_address = (localhost_ip, 50009)
sock.connect(sever_address)

f = open("PROJI-HNS.txt")
lines = f.readlines()
i = 0
for line in lines:
    #new_data = str("%s" % line).encode("utf-8")
    sock.send(line.encode())

    #time.sleep(2)

    data_from_server = sock.recv(100).decode()

        #list.append(data_from_rs[0].decode('utf-8'))
        #print(list)
    #hostname = set()
    #flag = set()
    #hostname.add(data_from_rs[0].decode('utf-8'))
    #flag.add(data_from_rs[2].decode('utf-8'))
    #hostname = data_from_rs[0].decode('utf-8')
    #flag = data_from_rs[2].decode('utf-8')
    #print (data_from_server.decode('utf-8'))
    print("Got from RS: %s" %(data_from_server))
    if(data_from_server[-2::]=="NS"):
        #print("get new one ")
        for attempt in range(1):
            try:
                ts.send(line.encode('utf-8'))
                server2_reply = ts.recv(1024).decode()
                print("Got from TS: %s" % ( server2_reply))
                results.append(server2_reply)
                f = open("RESOLVED.txt", 'a')
                f.write(server2_reply)
                f.write('\n')
                break
            except:
                # open new socket
                try:
                    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                except socket.error as err:
                    print('socket open error: {} \n'.format(err))
                    exit()


                tsServer_addr = socket.gethostbyname(socket.gethostname())
                tsServer_binding = (tsServer_addr, 50010)
                ts.connect(tsServer_binding)
    else:
        f = open("RESOLVED.txt", 'a')
        f.write(data_from_server)
        f.write('\n')
        results.append(data_from_server)
print(results)

ts.close()
sock.close()
f.close()