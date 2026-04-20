import unittest
from unittest.mock import patch

from core.firewall import Firewall

class TestFirewall(unittest.TestCase):

    @patch("subprocess.run")
    def test_block_ip_linux(self, mock_run):
        fw = Firewall()
        fw.os_type = "linux"

        result = fw.block_ip("192.168.1.100")
        self.assertTrue(result)
        mock_run.assert_called()

    @patch("subprocess.run")
    def test_unblock_ip_linux(self, mock_run):
        fw = Firewall()
        fw.os_type = "linux"

        result = fw.unblock_ip("192.168.1.100")
        self.assertTrue(result)
        mock_run.assert_called()

    @patch("subprocess.run")
    def test_block_ip_windows(self, mock_run):
        fw = Firewall()
        fw.os_type = "windows"

        result = fw.block_ip("192.168.1.100")
        self.assertTrue(result)
        mock_run.assert_called()

    @patch("subprocess.run")
    def test_unblock_ip_windows(self, mock_run):
        fw = Firewall()
        fw.os_type = "windows"

        result = fw.unblock_ip("192.168.1.100")
        self.assertTrue(result)
        mock_run.assert_called()

    def test_unsupported_os(self):
        fw = Firewall()
        fw.os_type = "darwin"

        self.assertFalse(fw.block_ip("192.168.1.100"))
        self.assertFalse(fw.unblock_ip("192.168.1.100"))

if __name__ == "__main__":
    unittest.main()
