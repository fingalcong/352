import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localhost_ip = socket.gethostbyname(local_hostname)

print("working on %s with %s" % (local_hostname, localhost_ip))

sever_address = (localhost_ip, 50007)
sock.bind(sever_address)

sock.listen(1)

while True:
    print ("wait for a connection")
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        while True:
            #data = connection.recv(100)
            data = connection.recv(100).decode()
            data_reverse = data[::-1] + data
            #connection.sendall(bytesdata_reverse.encode('utf-8'))
            connection.sendall(bytes(data_reverse, 'utf-8'))
            if data:
                print ("data received: %s" %data)
            else:
                print("done")
                break
    finally:
        connection.close()