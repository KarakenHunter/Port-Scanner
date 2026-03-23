# Advanced TCP Port Scanner

A multi-threaded TCP port scanner built using Python. This tool scans a given range of ports on a target system and identifies open ports along with optional banner grabbing.

## Features
- Multi-threaded scanning for faster performance
- Configurable port range
- Timeout handling
- Banner grabbing for service detection
- Logs results to file
- Displays scan duration

## Technologies Used
- Python
- Socket Programming
- ThreadPoolExecutor (Concurrency)

## How to Run

```bash
python scanner.py
Enter:

Target IP
Start port
End port

Example Output
[+] Port 80 OPEN | HTTP
[+] Port 443 OPEN | HTTPS
```
Disclaimer:
This tool is for educational purposes only. Use it only on systems you own or have permission to test.
