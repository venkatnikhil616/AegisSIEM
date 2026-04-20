from flask import request, jsonify
from api.auth import require_api_key

from integrations.firewall_adapter import FirewallAdapter
from services.report_service import ReportService
from services.threat_intel_service import ThreatIntelService

firewall = FirewallAdapter()
report_service = ReportService()
threat_intel = ThreatIntelService()


def register_routes(app):
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    @app.route("/block", methods=["POST"])
    @require_api_key
    def block_ip():
        data = request.json
        ip = data.get("ip")
        if not ip:
            return jsonify({"error": "Missing IP"}), 400

        result = firewall.block(ip)
        return jsonify({"ip": ip, "blocked": result})

    @app.route("/unblock", methods=["POST"])
    @require_api_key
    def unblock_ip():
        data = request.json
        ip = data.get("ip")
        if not ip:
            return jsonify({"error": "Missing IP"}), 400

        result = firewall.unblock(ip)
        return jsonify({"ip": ip, "unblocked": result})

    @app.route("/blacklist", methods=["GET"])
    @require_api_key
    def get_blacklist():
        return jsonify({"blacklist": list(threat_intel.get_blacklist())})

    @app.route("/report", methods=["GET"])
    @require_api_key
    def generate_report():
        path = report_service.generate_detailed_report()
        return jsonify({"report_path": path})
