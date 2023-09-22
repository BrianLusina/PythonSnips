from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.histories: Dict[str, List[Tuple[int, str]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.histories:
            self.histories[key] = [(timestamp, value)]
            return
        self.histories[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.histories:
            return ""

        key_historical_values = self.histories[key]

        left, right, pos = 0, len(key_historical_values) - 1, -1

        while left <= right:
            mid = (left + right) // 2

            timestamp_value_at_mid = key_historical_values[mid]
            timestamp_for_value = timestamp_value_at_mid[0]

            if timestamp_for_value <= timestamp:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1

        if pos == -1:
            return ""

        return key_historical_values[pos][1]
