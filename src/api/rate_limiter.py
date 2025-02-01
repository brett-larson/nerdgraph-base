import time
from collections import deque
from datetime import datetime, timedelta


class RateLimiter:
    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.calls = deque()

    def wait_if_needed(self):
        now = datetime.now()
        # Remove calls older than 1 minute
        while self.calls and (now - self.calls[0]) > timedelta(minutes=1):
            self.calls.popleft()

        # If at limit, wait until oldest call is more than 1 minute old
        if len(self.calls) >= self.calls_per_minute:
            wait_time = (self.calls[0] + timedelta(minutes=1) - now).total_seconds()
            if wait_time > 0:
                time.sleep(wait_time)

        self.calls.append(now)