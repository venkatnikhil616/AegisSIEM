import time
from core.attack_simulator import AttackSimulator
from core.parser import PacketParser
from core.detector import ThreatDetector
from core.response_engine import ResponseEngine
from core.correlation_engine import CorrelationEngine
from core.soc_dashboard import SOCDashboard

class Listener:
    def __init__(self):
        self.source = AttackSimulator()
        self.parser = PacketParser()
        self.detector = ThreatDetector()
        self.responder = ResponseEngine()
        self.correlation = CorrelationEngine()
        self.dashboard = SOCDashboard()

        self.running = True
        self.max_events = 120   # 🔥 prevents infinite execution

    def start(self):
        print("\n[SIEM] CONTROLLED ENGINE STARTED\n")

        event_count = 0
        last_refresh = 0

        while self.running:

            # 🛑 STOP CONDITION (VERY IMPORTANT)
            if event_count >= self.max_events:
                print("\n[SIEM] EVENT LIMIT REACHED → STOPPING ENGINE\n")
                break

            packet = self.source.generate_packet()
            parsed = self.parser.parse(packet)

            if not parsed:
                continue

            threat = self.detector.analyze(parsed)
            correlation = self.correlation.analyze(parsed)

            # 🚨 alert condition
            if threat.get("malicious") or correlation.get("correlated"):
                self.responder.handle(threat, parsed)

            event_count += 1

            # 🧊 slow processing (prevents infinite CPU loop)
            time.sleep(0.2)

            # 📊 dashboard refresh every 2 seconds
            now = time.time()
            if now - last_refresh > 2:
                self.dashboard.render()
                last_refresh = now
