import socket
import errno

for port in range(1, 65536):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex(('localhost', port))
    if result == 0:
        print(f"[+] Port {port} OPEN")
    elif result == errno.ECONNREFUSED:
        print(f"[-] Port {port} is CLOSED")
    elif result == errno.ETIMEDOUT:
        print(f"[?] Port {port} FILTERED")
    else:
        print(f"[!] Port {port} UNKNOWN ({result})")
    sock.close()