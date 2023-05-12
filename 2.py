
global dns_table, key

f = open("PROJI-DNSRS.txt")
file = f.readlines()
for line in file:
            temp_line = line.split()
            hostname = temp_line[0].lower()
            ip = temp_line[1]
            flag = temp_line[2]
            dns_table[hostname] = [ip, flag]
            print(temp_line[2])


f1 = open("PROJI-HNS.txt")
hostname = f1.readline().strip('\n')
if hostname in dns_table:
        ip = dns_table[hostname][0]
        flag = dns_table[hostname][1]
        print (hostname + " " + ip + " " + flag)
else:
        print (hostname + " - " + "Error:HOSTNOTFOUND")









    data_from_rs = data_from_server.split()
    if data_from_rs[2] == 'NS':
         sock.sendall(data_from_rs[0])

    data_from_TS = sock.recv(100)
    print("Got from TS:{}".format(data_from_TS.decode('utf-8')))