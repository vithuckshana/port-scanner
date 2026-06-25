# 🔍 Python Multi-Threaded Port Scanner

A beginner-friendly cybersecurity project that demonstrates how port scanning works using Python sockets and multithreading.

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**.  
Only scan devices you own or have permission to test.

Unauthorized scanning of external systems may be illegal.

---

## 🚀 Features

- TCP port scanning using Python sockets
- Multi-threaded scanning (ThreadPoolExecutor)
- Fast performance with controlled concurrency
- Service detection for common ports
- Simple command-line interface (CLI)

---

## 🧠 What I Learned

- IP addresses and ports
- TCP connection basics
- Python socket programming
- Multithreading in Python
- Basic network reconnaissance concepts

---

## 📌 Common Ports Detected

| Port | Service |
|------|--------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 53   | DNS     |
| 80   | HTTP    |
| 443  | HTTPS   |

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/port-scanner.git
```

### 2. Navigate into the folder
```bash
cd port-scanner
```

### 3. Run the program
```bash
python port_scanner.py
```

---

## 📥 Example Output

```
Enter target IP: 127.0.0.1
Start port: 1
End port: 100

Scanning target: 127.0.0.1
----------------------------
[OPEN] Port 135 → Unknown Service
[OPEN] Port 445 → Unknown Service

Scan Complete!
Total Open Ports: 2
```

---

## ⚙️ Tech Stack

- Python 3
- socket library
- concurrent.futures (ThreadPoolExecutor)

---

## 📁 Project Structure

```
port-scanner/
│
├── port_scanner.py
├── README.md
└── scan_results.txt (generated after run)
```

---

## 👨‍💻 Author

Beginner Cybersecurity Learner  
Building foundational networking & security tools step by step.