import socket
import errno
import time
from concurrent.futures import ThreadPoolExecutor

start_time = time.time()
target = input("Enter target IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            line = f"[+] Port {port} OPEN | {banner}\n"
            print(line.strip())
            with open("Logs.txt", "a") as f:
                f.write(line)
        elif result == errno.ETIMEDOUT:
            line = f"[?] Port {port} FILTERED\n"
            with open("Logs.txt", "a") as f:
                f.write(line)
        sock.close()
    except:
        pass

print(f"\nScanning {target} from port {start} to {end}...\n")
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start, end+1))
print("\nScan Completed. Results saved in Logs.txt")
print(f"Time taken: {time.time() - start_time:.2f} seconds")
