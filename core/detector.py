class ThreatDetector:
    def analyze(self, packet):

        attack_type = packet.get("type", "NORMAL")

        if attack_type == "NORMAL":
            return {"malicious": False}

        score = 0

        if attack_type == "SYN_FLOOD":
            score = 7
        elif attack_type == "PORT_SCAN":
            score = 6
        elif attack_type == "DDOS_SPIKE":
            score = 9

        return {
            "malicious": True,
            "type": attack_type,
            "src_ip": packet.get("src_ip"),
            "score": score
        }
