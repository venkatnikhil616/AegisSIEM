import json
import os
from datetime import datetime

class ReportService:
    def __init__(self, logs_dir="logs", reports_dir="reports"):
        self.logs_dir = logs_dir
        self.reports_dir = reports_dir
        os.makedirs(self.reports_dir, exist_ok=True)

    def _read_log(self, filename):
        path = os.path.join(self.logs_dir, filename)
        if not os.path.exists(path):
            return []

        with open(path, "r") as f:
            return f.readlines()

    def generate_summary(self):
        activity_logs = self._read_log("activity.log")
        alert_logs = self._read_log("alerts.log")
        error_logs = self._read_log("errors.log")

        summary = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_activity_events": len(activity_logs),
            "total_alerts": len(alert_logs),
            "total_errors": len(error_logs)
        }

        return summary

    def generate_detailed_report(self):
        report = {
            "summary": self.generate_summary(),
            "activity_logs": self._read_log("activity.log"),
            "alert_logs": self._read_log("alerts.log"),
            "error_logs": self._read_log("errors.log")
        }

        filename = f"report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        path = os.path.join(self.reports_dir, filename)

        with open(path, "w") as f:
            json.dump(report, f, indent=2)

        return path
