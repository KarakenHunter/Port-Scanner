import socket
import errno

with open("Logs.txt", 'a') as f:
    for port in range(1, 65536):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result=sock.connect_ex(('localhost', port))
        if result == 0:
            f.write(f"[+] Port {port} OPEN\n")
        elif result == errno.ECONNREFUSED:
            pass
        elif result == errno.ETIMEDOUT:
            f.write(f"[?] Port {port} FILTERED")
        else:
            f.write(f"[!] Port {port} UNKNOWN ({result})")
        sock.close()
print("Data Successfully saved in Logs.txt!")