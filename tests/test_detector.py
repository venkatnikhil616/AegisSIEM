import unittest
import time

from core.detector import ThreatDetector

class TestThreatDetector(unittest.TestCase):

    def setUp(self):
        self.detector = ThreatDetector()

    def test_normal_traffic(self):
        packet = {
            "src_ip": "192.168.1.10",
            "dst_port": 80
        }

        result = self.detector.analyze(packet)
        self.assertFalse(result["malicious"])

    def test_rate_limit_exceeded(self):
        packet = {
            "src_ip": "10.0.0.1",
            "dst_port": 80
        }

        for _ in range(self.detector.rate_limit_threshold + 1):
            result = self.detector.analyze(packet)

        self.assertTrue(result["malicious"])
        self.assertEqual(result["reason"], "RATE_LIMIT_EXCEEDED")

    def test_port_scan_detection(self):
        ip = "172.16.0.5"

        for port in range(self.detector.port_scan_threshold + 1):
            packet = {
                "src_ip": ip,
                "dst_port": port
            }
            result = self.detector.analyze(packet)

        self.assertTrue(result["malicious"])
        self.assertEqual(result["reason"], "PORT_SCAN_DETECTED")

    def test_blacklisted_ip(self):
        ip = "203.0.113.99"
        self.detector.blocked_ips.add(ip)

        packet = {
            "src_ip": ip,
            "dst_port": 80
        }

        result = self.detector.analyze(packet)
        self.assertTrue(result["malicious"])
        self.assertEqual(result["reason"], "BLACKLISTED_IP")

if __name__ == "__main__":
    unittest.main()
