from datetime import timedelta, datetime, UTC
from threading import Lock


class CircuitBreaker:
    """
    Circuit breaker pattern to prevent cascading failures.
    Stops processing if error rate exceeds threshold.
    """

    def __init__(
        self, failure_threshold: int = 5, timeout: timedelta = timedelta(seconds=60)
    ):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        self.lock = Lock()

    def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        with self.lock:
            if self.state == "OPEN":
                if datetime.now(UTC) - self.last_failure_time > self.timeout:
                    self.state = "HALF_OPEN"
                else:
                    raise Exception("Circuit breaker is OPEN")

        try:
            result = func(*args, **kwargs)
            with self.lock:
                if self.state == "HALF_OPEN":
                    self.state = "CLOSED"
                    self.failure_count = 0
            return result
        except Exception as e:
            with self.lock:
                self.failure_count += 1
                self.last_failure_time = datetime.now(UTC)
                if self.failure_count >= self.failure_threshold:
                    self.state = "OPEN"
            raise e
