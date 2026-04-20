import subprocess
import platform

class Firewall:
    def __init__(self):
        self.os_type = platform.system().lower()

    def block_ip(self, ip):
        if self.os_type == "linux":
            return self._block_ip_linux(ip)
        elif self.os_type == "windows":
            return self._block_ip_windows(ip)
        else:
            return False

    def unblock_ip(self, ip):
        if self.os_type == "linux":
            return self._unblock_ip_linux(ip)
        elif self.os_type == "windows":
            return self._unblock_ip_windows(ip)
        else:
            return False

    def _block_ip_linux(self, ip):
        try:
            subprocess.run(
                ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except:
            return False

    def _unblock_ip_linux(self, ip):
        try:
            subprocess.run(
                ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except:
            return False

    def _block_ip_windows(self, ip):
        try:
            subprocess.run(
                [
                    "netsh", "advfirewall", "firewall",
                    "add", "rule",
                    f"name=Block_{ip}",
                    "dir=in",
                    "action=block",
                    f"remoteip={ip}"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                shell=True
            )
            return True
        except:
            return False

    def _unblock_ip_windows(self, ip):
        try:
            subprocess.run(
                [
                    "netsh", "advfirewall", "firewall",
                    "delete", "rule",
                    f"name=Block_{ip}"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                shell=True
            )
            return True
        except:
            return False
