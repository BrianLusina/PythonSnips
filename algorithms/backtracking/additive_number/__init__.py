def is_additive_number_dfs(num: str) -> bool:
    if not num:
        return False

    n = len(num)

    def dfs(a: int, b: int, number: str) -> bool:
        if not number:
            return True

        if a + b > 0 and number[0] == "0":
            return False

        for i in range(1, len(number) + 1):
            if a + b == int(number[:i]):
                if dfs(b, a + b, number[i:]):
                    return True
        return False

    for x in range(1, n - 1):
        for y in range(x + 1, n):
            if x > 1 and num[0] == "0":
                break
            if y - x > 1 and num[x] == "0":
                continue
            if dfs(int(num[:x]), int(num[x:y]), num[y:]):
                return True

    return False


def is_additive_number_backtrack(num: str) -> bool:
    n = len(num)

    def backtrack(start: int, prev1: int, prev2: int, count: int) -> bool:
        # Base case: we've consumed the entire string
        if start == n:
            # Valid only if we have at least 3 numbers in the sequence
            return count >= 3

        # Try every possible next number by varying its length
        for end in range(start + 1, n + 1):
            # Extract the substring representing the current number
            substring = num[start:end]

            # Skip numbers with leading zeros (e.g., "03"), but "0" itself is allowed
            if len(substring) > 1 and substring[0] == "0":
                break  # No point trying longer substrings; they'll also have leading zero

            current_num = int(substring)

            # If we already have at least 2 numbers, validate the additive property
            if count >= 2:
                expected_sum = prev1 + prev2

                # If current number is too large, no need to try longer substrings
                if current_num > expected_sum:
                    break

                # If current number doesn't match the expected sum, try next length
                if current_num < expected_sum:
                    continue

                # current_num == expected_sum, so recurse with updated sequence

            # Recurse: prev2 becomes prev1, current_num becomes the new prev2
            if backtrack(end, prev2, current_num, count + 1):
                return True

        return False

    # Start backtracking from index 0 with no previous numbers and count = 0
    return backtrack(0, 0, 0, 0)
