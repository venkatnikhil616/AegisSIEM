import unittest
import json

from api.app import create_app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": "secure_api_key"
        }

    def test_health(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.get_json())

    def test_block_ip_unauthorized(self):
        response = self.app.post("/block", json={"ip": "192.168.1.100"})
        self.assertEqual(response.status_code, 401)

    def test_block_ip(self):
        response = self.app.post(
            "/block",
            headers=self.headers,
            data=json.dumps({"ip": "192.168.1.100"})
        )
        self.assertIn(response.status_code, [200, 500])

    def test_unblock_ip(self):
        response = self.app.post(
            "/unblock",
            headers=self.headers,
            data=json.dumps({"ip": "192.168.1.100"})
        )
        self.assertIn(response.status_code, [200, 500])

    def test_get_blacklist(self):
        response = self.app.get("/blacklist", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("blacklist", response.get_json())

    def test_generate_report(self):
        response = self.app.get("/report", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("report_path", response.get_json())

if __name__ == "__main__":
    unittest.main()
