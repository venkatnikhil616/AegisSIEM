from collections import defaultdict
import time

class CorrelationEngine:
    def __init__(self):
        self.ip_tracker = defaultdict(list)

    def analyze(self, event):
        ip = event.get("src_ip")
        attack_type = event.get("type")

        now = time.time()

        if ip:
            self.ip_tracker[ip].append(now)

            # remove old entries (last 10 sec window)
            self.ip_tracker[ip] = [
                t for t in self.ip_tracker[ip] if now - t < 10
            ]

            # 🔥 CORRELATION RULE: rapid requests = attack
            if len(self.ip_tracker[ip]) > 5:
                return {
                    "correlated": True,
                    "type": "BEHAVIORAL_SPIKE",
                    "src_ip": ip,
                    "confidence": 90
                }

        # pattern-based correlation
        if attack_type == "PORT_SCAN":
            return {
                "correlated": True,
                "type": "SCAN_ACTIVITY",
                "src_ip": ip,
                "confidence": 70
            }

        return {"correlated": False}
