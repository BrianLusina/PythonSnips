def find_kth_number(n: int, k: int) -> int:
    curr = 1
    k -= 1

    # To count how many numbers exist between prefix1 and prefix2
    def count_steps(prefix1: int, prefix2: int) -> int:
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps

    while k > 0:
        step = count_steps(curr, curr + 1)
        # If the steps are less than or equal to k, we skip this prefix's subtree
        if step <= k:
            # Move to the next prefix and decrease k by the number of steps we skip
            curr += 1
            k -= step
        else:
            # Move to the next level of the tree and decrement k by 1
            curr *= 10
            k -= 1

    return curr


def find_kth_number_2(n: int, k: int) -> int:
    """
    Find the k-th smallest number in lexicographical order from 1 to n.

    Args:
        n: The upper bound of the range [1, n]
        k: The position of the number to find (1-indexed)

    Returns:
        The k-th smallest number in lexicographical order
    """

    def count_steps_between_prefixes(current_prefix: int) -> int:
        """
        Count how many numbers exist in the lexicographical range
        starting with current_prefix up to the next prefix.

        For example, if current_prefix = 1, this counts all numbers
        starting with 1 (like 1, 10, 11, ..., 19, 100, 101, ...)
        up to but not including those starting with 2.

        Args:
            current_prefix: The current prefix to count from

        Returns:
            Number of valid numbers with this prefix within range [1, n]
        """
        next_prefix = current_prefix + 1
        steps_count = 0

        # Count numbers at each level of the tree
        # Level 1: single digits (1-9)
        # Level 2: double digits (10-99)
        # Level 3: triple digits (100-999), etc.
        while current_prefix <= n:
            # Count valid numbers at this level
            # Either count all numbers between current_prefix and next_prefix-1
            # Or stop at n if it's smaller
            steps_count += min(n - current_prefix + 1, next_prefix - current_prefix)

            # Move to next level (add a digit)
            next_prefix *= 10
            current_prefix *= 10

        return steps_count

    # Start with number 1
    current_number = 1

    # We've already counted the first number (1), so decrement k
    k -= 1

    # Find the k-th number by navigating the lexicographical tree
    while k > 0:
        # Count how many numbers are under the current prefix
        steps_to_next_prefix = count_steps_between_prefixes(current_number)

        if k >= steps_to_next_prefix:
            # Skip entire subtree and move to next sibling
            k -= steps_to_next_prefix
            current_number += 1  # Move to next prefix at same level
        else:
            # The target is within current subtree, go deeper
            k -= 1  # Count current number
            current_number *= 10  # Go to first child (append 0)

    return current_number


def find_kth_number_3(n, k):
    # Start from number 1 (the smallest lexicographical number)
    current_number = 1

    # We already count '1' as the first number, so decrease k by 1
    k -= 1

    # Helper function to count how many numbers are in the range [prefix_start, prefix_end) in lex order
    def count_numbers_under_prefix(prefix_start, prefix_end):
        numbers_under_prefix = 0

        # Loop through each level of the number tree (1-digit, 2-digit, etc.)
        while prefix_start <= n:
            # Count numbers in this range, but don't go beyond n
            # At each level, we calculate the range [prefix_start, prefix_end)
            # For example: 1 to 2, 10 to 20, 100 to 200, etc.
            numbers_under_prefix += min(n + 1, prefix_end) - prefix_start

            # Go one level deeper by multiplying by 10
            # This simulates moving to the next digit depth
            prefix_start *= 10
            prefix_end *= 10

        # Total count of valid numbers under the original prefix
        return numbers_under_prefix

    # Loop until we've found the k-th number
    while k > 0:
        # Calculate how many numbers are in the current subtree (numbers starting with current_number)
        numbers_under_prefix = count_numbers_under_prefix(
            current_number, current_number + 1
        )

        # If k is in the child subtree, go deeper to move to the first child
        # (i.e., next digit level in the same prefix)
        # For example, from 1 -> 10 -> 100...
        if k < numbers_under_prefix:
            # Move down one level
            current_number *= 10

            # Reduce k by 1
            k -= 1

        # Otherwise, if k is in the sibling subtree, i.e., if there are fewer or equal numbers than k under current prefix,
        # move to the next sibling by skipping this whole prefix subtree
        else:
            # Move to the next sibling
            current_number += 1

            # Reduce k by how many numbers we skipped
            k -= numbers_under_prefix

    # This is the k-th number in lexicographical order
    return current_number
