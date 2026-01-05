from typing import Dict


class RequestLogger:
    def __init__(self, time_limit: int):
        self.time_limit = time_limit
        # keeps track of the requests as they come in key value pairs, which allows for first lookups (O(1)).
        # the key is the request, the value is the time.
        self.request_map: Dict[str, int] = {}

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp: int, request: str) -> bool:
        formatted_message = request.lower()
        if formatted_message in self.request_map:
            latest_time_for_message = self.request_map[formatted_message]
            difference = timestamp - latest_time_for_message
            if difference < self.time_limit:
                return False
            self.request_map[formatted_message] = timestamp
            return True

        self.request_map[formatted_message] = timestamp
        return True
