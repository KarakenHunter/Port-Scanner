import socket
i=0
while i<=100:
    try:
        is_socket=None
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect_ex(('localhost', i))
        is_socket=True
        if is_socket==True:
            print(f"Port {i} is open")
        i+=1
    except:
        i+=1

