import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests=100, window_seconds=10):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(lambda: deque())

    def check(self, key):
        current_time = time.time()
        q = self.requests[key]

        while q and current_time - q[0] > self.window_seconds:
            q.popleft()

        q.append(current_time)

        if len(q) > self.max_requests:
            return {
                "limited": True,
                "reason": "RATE_LIMIT_EXCEEDED",
                "key": key,
                "count": len(q),
                "window": self.window_seconds
            }

        return {"limited": False}
