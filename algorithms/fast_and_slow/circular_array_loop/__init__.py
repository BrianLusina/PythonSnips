from typing import List


def circular_array_loop(nums: List[int]) -> bool:
    """
    Checks if there is a cycle in the provided list of non-zero integers

    Problem Explanation:
    A cycle exists if we can start at an index and follow the direction of the array (either forward or backward) and
    return to the starting index without getting stuck in a loop that doesn't include all elements.

    The array is circular, meaning that if you reach the end of the array, you wrap around to the beginning, and vice
    versa.

    Algorithm:
    - Direction Check: Determine the direction of movement (forward or backward) based on the sign of the current
    element.
    - Cycle Detection: Use a slow and fast pointer approach (similar to Floyd's Tortoise and Hare algorithm) to detect
    a cycle.
    - Cycle Validation: Ensure that the cycle is valid (i.e., it covers all elements and is not a subset of the array).

    Time Complexity:
        The time complexity is O(n), where n is the length of the array. This is because each element is processed at
        most once.

    Space Complexity:
        The space complexity is O(1) since we are using a constant amount of extra space.

    Args:
        nums (list): list of non-zero integers
    Returns:
        bool: True if there is a circular array loop, False otherwise
    """
    length = len(nums)

    for i in range(length):
        # Skip if we've already visited this index
        if nums[i] == 0:
            continue

        # Determine the direction of the cycle based on the sign of the current element
        direction = 1 if nums[i] > 0 else -1

        # set the slow and the fast pointers to the current index
        slow, fast = i, i

        while True:
            # Move slow pointer
            slow = (slow + nums[slow]) % length

            if nums[slow] * direction <= 0:
                break  # Invalid direction

            # Move fast pointer twice

            # first time
            fast = (fast + nums[fast]) % length
            if nums[fast] * direction <= 0:
                break  # Invalid direction

            # second time
            fast = (fast + nums[fast]) % length
            if nums[fast] * direction <= 0:
                break  # Invalid direction

            # If slow and fast meet, a cycle is detected
            if slow == fast:
                # Check if the cycle length is greater than 1
                if slow == (slow + nums[slow]) % length:
                    break  # Cycle length is 1, invalid
                return True

        # Mark all visited indices in this path to avoid reprocessing
        # Note that this modifies the input list of elements and may not be desirable. This however, has a space
        # complexity of O(1) as no extra space is allocated. An alternative solution is to use a list to keep track of
        # visited indices and avoid reprocessing, this list would be initialized the the length of the input list such
        # as visited = [0 for _ in range(length)] or visited = [False for _ in range(length)] or
        # visited = [False] * length
        # and then that is used to avoid reprocessing like below:
        # while nums[slow] * direction > 0 and not visited[slow]:
        #   visited[slow] = True
        #   slow = (slow + nums[slow]) % length
        slow = i
        while nums[slow] * direction > 0:
            next_slow = (slow + nums[slow]) % length
            nums[slow] = 0
            slow = next_slow

    return False
