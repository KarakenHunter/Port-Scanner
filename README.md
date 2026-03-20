# TCP Port Scanner (Python)

##  Overview

A simple TCP port scanner built using Python sockets.
This tool scans a range of ports on a target host and identifies:

* Open ports
* Filtered ports
* Unknown responses

Closed ports are intentionally ignored to keep output concise and focused.

---

##  Features

* TCP-based port scanning using `socket`
* Timeout handling to avoid hanging on filtered ports
* Error-based port classification using `errno`
* Logs results directly to a file (`Logs.txt`)
* Efficient logging (only relevant ports stored)

---

##  How It Works

The scanner attempts to establish a TCP connection with each port:

* **Success (0)** → Port is OPEN
* **Connection Refused** → Port is CLOSED (ignored)
* **Timeout** → Port is FILTERED (likely firewall)
* **Other errors** → Marked as UNKNOWN

---

##  Usage

Run the script:

```bash
python scanner.py
```

By default, it scans:

* Host: `localhost`
* Ports: `1 → 65535`

---

##  Output

Results are saved in:

```bash
Logs.txt
```

Example:

```
[+] Port 22 OPEN
[?] Port 25 FILTERED
[!] Port 8080 UNKNOWN (101)
```

---

##  Design Decisions

*  Closed ports are not logged → reduces noise and file size
*  File is opened once → better performance
*  Each socket is properly closed → prevents resource leaks

---

##  Limitations

* Single-threaded (slower for full port range scans)
* No CLI support for custom targets (yet)
* Basic TCP connect scan (not stealthy like SYN scan)

---

##  Future Improvements

* Multi-threaded scanning for speed
* CLI support for target and port range
* Banner grabbing for service detection
* Output formats (JSON / CSV)

---

##  Requirements

* Python 3.x
* No external libraries required

---
