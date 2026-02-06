from typing import List


def can_cross(stones: List[int]) -> bool:
    n = len(stones)

    # Map each stone's position to its index for O(1) lookups
    mapper = {stones[i]: i for i in range(n)}

    # dp[i][k] = 1 if the frog can reach stone i with a jump of length k
    dp = [[0] * 2001 for _ in range(2001)]
    dp[0][0] = 1  # Starting point: frog at first stone with jump size 0

    # Try to reach every stone using all possible previous jump sizes
    for i in range(n):
        for prev_jump in range(n + 1):
            if dp[i][prev_jump]:
                curr_pos = stones[i]

                # Jump of the same length
                if curr_pos + prev_jump in mapper:
                    dp[mapper[curr_pos + prev_jump]][prev_jump] = 1

                # Jump one unit longer
                if curr_pos + prev_jump + 1 in mapper:
                    dp[mapper[curr_pos + prev_jump + 1]][prev_jump + 1] = 1

                # Jump one unit shorter (if valid)
                if prev_jump > 1 and curr_pos + prev_jump - 1 in mapper:
                    dp[mapper[curr_pos + prev_jump - 1]][prev_jump - 1] = 1

    # Check if the last stone is reachable with any jump size
    for jump in range(n + 1):
        if dp[n - 1][jump]:
            return True

    # If no valid path reaches the last stone
    return False
