# Enforcer-IPS Architecture

## Overview
Enforcer-IPS is a real-time Intrusion Prevention System designed to monitor, detect, and block malicious network traffic.

## Components

### 1. Packet Capture Layer
- packet_sniffer.py captures live traffic

### 2. Processing Layer
- parser.py extracts structured data
- detector.py analyzes threats

### 3. Detection Engine
- Signature-based detection
- Rate limiting
- Port scan detection
- Anomaly detection

### 4. Response Layer
- firewall.py blocks malicious IPs
- response_engine.py manages actions

### 5. Services
- alert_service.py → notifications
- log_service.py → logging
- threat_intel_service.py → external threat feeds

### 6. API & Dashboard
- REST API for control
- Dashboard for monitoring logs

## Flow
Packet → Parser → Detector → Response → Firewall/Alert
