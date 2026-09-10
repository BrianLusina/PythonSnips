from typing import List


def last_stone_weight_2(stones: List[int]) -> int:
    # Calculate the total sum of all stones
    total_sum = sum(stones)

    # Number of stones and target sum (half of total)
    num_stones = len(stones)
    target = total_sum // 2

    # DP table: dp[i][j] represents the maximum sum we can achieve
    # using first i stones with sum not exceeding j
    dp = [[0] * (target + 1) for _ in range(num_stones + 1)]

    # Fill the DP table
    for i in range(1, num_stones + 1):
        for j in range(target + 1):
            # Option 1: Don't include the current stone
            dp[i][j] = dp[i - 1][j]

            # Option 2: Include the current stone if it fits
            if stones[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])

    # The minimum difference is: total_sum - 2 * maximum_sum_in_one_subset
    # This works because if we partition stones into two groups with sums S1 and S2,
    # where S1 <= S2, then S1 + S2 = total_sum and the difference is S2 - S1
    # We want to maximize S1 (up to total_sum/2), so S2 - S1 = total_sum - 2*S1
    return total_sum - 2 * dp[num_stones][target]


def last_stone_weight_2_2(stones: List[int]) -> int:
    # Calculate total sum of all stones
    total_sum = sum(stones)

    # Target is half of the total sum (we want to split stones into two groups as equal as possible)
    target = total_sum // 2

    # dp[j] = True if we can achieve sum j using some subset of stones
    dp = [False] * (target + 1)

    # Base case: sum of 0 is always achievable (empty subset)
    dp[0] = True

    # Iterate over each stone
    for stone in stones:
        # Traverse target down to stone value to avoid using same stone twice (0/1 knapsack)
        for j in range(target, stone - 1, -1):
            # Mark j as achievable if j-stone was previously achievable
            dp[j] = dp[j] or dp[j - stone]

    # Find the largest sum <= target that is achievable
    for s in range(target, -1, -1):
        if dp[s]:
            # s = one group's sum, totalSum - s = other group's sum
            # Minimum remaining stone = difference between the two groups
            return total_sum - 2 * s

    # Fallback (should never reach here given constraints)
    return 0
