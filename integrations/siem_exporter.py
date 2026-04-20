import json
import socket
import time

class SIEMExporter:
    def __init__(self, host="127.0.0.1", port=514, protocol="udp"):
        self.host = host
        self.port = port
        self.protocol = protocol.lower()

    def _format_event(self, event):
        return json.dumps({
            "timestamp": time.time(),
            "event": event
        })

    def send(self, event):
        message = self._format_event(event).encode()

        try:
            if self.protocol == "udp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(message, (self.host, self.port))
                sock.close()
            elif self.protocol == "tcp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.host, self.port))
                sock.sendall(message)
                sock.close()
            return True
        except:
            return False
