import threading
from queue import Queue

from scapy.all import sniff

class PacketSniffer:
    def __init__(self, interface="lo", queue: Queue = None):
        self.interface = interface
        self.queue = queue or Queue()
        self.running = False

    def _packet_callback(self, packet):
        if not self.running:
            return

        try:
            self.queue.put(packet, block=False)
        except Exception:
            pass

    def start(self):
        self.running = True

        print(f"[+] Sniffing on interface: {self.interface}")

        sniff(
            iface=self.interface,
            prn=self._packet_callback,
            store=False,
            stop_filter=lambda x: not self.running
        )

    def stop(self):
        self.running = False
