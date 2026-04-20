from flask import Flask, jsonify
from core.shared_state import log_queue, alert_queue

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>ENFORCER IPS DASHBOARD</h1>
    <p>Status: Running</p>
    <a href='/logs'>Logs</a> | <a href='/alerts'>Alerts</a>
    """

@app.route("/logs")
def logs():
    items = []
    while not log_queue.empty():
        items.append(log_queue.get())
    return jsonify(items)

@app.route("/alerts")
def alerts():
    items = []
    while not alert_queue.empty():
        items.append(alert_queue.get())
    return jsonify(items)

# ✅ THIS IS THE MISSING PART
if __name__ == "__main__":
    print("[DASHBOARD] Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=False)
