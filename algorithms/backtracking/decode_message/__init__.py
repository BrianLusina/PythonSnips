from typing import Dict


def number_of_ways_to_decode_message(digits: str) -> int:
    """Finds the number of ways to decode a message given digits from 1-9

    Time Complexity
    The time complexity of the memoization solution is the size of the memo array O(n) multiplied by the number of
    operations per state which is O(1). So the overall time complexity is O(n).

    Space Complexity
    The height of the state-space tree is at most O(n). The size of the memo array is O(n). Therefore the space
    complexity is O(n).
    """
    memo: Dict[int, int] = {}

    def dfs(start_index: int) -> int:
        if start_index in memo:
            return memo[start_index]

        if start_index == len(digits):
            return 1

        ways = 0

        # can't decode string with leading 0
        if digits[start_index] == "0":
            return ways

        # decode 1 digit
        ways += dfs(start_index + 1)

        # decode 2 digits
        if 10 <= int(digits[start_index : start_index + 2]) <= 26:
            ways += dfs(start_index + 2)

        memo[start_index] = ways
        return ways

    return dfs(0)
