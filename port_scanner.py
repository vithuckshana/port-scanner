import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning target:", target)
print("----------------------------")

open_ports = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    sock.close()

# Thread Pool (controlled concurrency)
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\nScan Complete!")
print("Total Open Ports:", len(open_ports))