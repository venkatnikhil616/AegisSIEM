import json
import time
from collections import deque


class EventStore:
    _instance = None  # 🔥 singleton storage

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventStore, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.events = deque(maxlen=200)
        self.file = "siem_logs.jsonl"

    def add_event(self, event):
        event["timestamp"] = time.time()

        self.events.append(event)

        try:
            with open(self.file, "a") as f:
                f.write(json.dumps(event) + "\n")
        except:
            pass

    def get_recent(self, n=50):
        return list(self.events)[-n:]
