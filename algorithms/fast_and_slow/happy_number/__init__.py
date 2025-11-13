def is_happy_number(n: int) -> bool:
    """
    Checks if an unsigned integer is a happy number

    A happy number is defined by the following process:
    - Replace the number by the sum of the squares of its digits.
    - Repeat the process until the number becomes 1 (happy number)
      or a cycle is detected (not a happy number).

    This uses a set to store already seen numbers which consumes extra space. But since the numbers may not be too
    large, using a set might be straightforward and easy to implement

    While this approach works well for small numbers, we might have to perform several computations for larger numbers
    to get the required result. So, it might get infeasible for such cases. The time complexity of this approach is
    O(log(n)). The space complexity is O(log(n)) since we're using additional space to store our calculated sums.

    Args:
        n (int): a positive integer
    Returns:
        bool: True if n is a happy number, False otherwise
    """

    def get_next(number: int) -> int:
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1


def is_happy_number_2(n: int) -> bool:
    """
    Checks if an unsigned integer is a happy number

    To determine whether a number is a happy number, it is iteratively replaced by the sum of the squares of its digits,
    forming a sequence of numbers. This sequence either converges to 1 (if the number is happy) or forms a cycle
    (if the number is not happy). We use the fast and slow pointers technique to detect such cycles efficiently.
    This technique involves advancing two pointers through the sequence at different speeds: one moving one step at a
    time and the other two at a time.

    The pointer moving slower is initialized to the given number, and the faster one starts at the sum of the squared
    digits of the given number. Then, in each subsequent iteration, the slow pointer updates to the sum of squared
    digits of itself, while the fast pointer advances two steps ahead: first by updating to the sum of squared digits
    of itself and then to the sum of squared digits of this recently calculated sum. If the number is happy, the fast
    pointer will eventually reach 1.

    However, if the number is not happy, indicating the presence of a cycle in the sequence, both pointers will
    eventually meet. This is because, in the non-cyclic part of the sequence, the distance between the pointers
    increases by one number in each iteration. Once both pointers enter the cyclic part, the faster pointer starts
    closing the gap on the slower pointer, decreasing the distance by one number in each iteration until they meet.
    This way, we can efficiently determine whether a number is a happy number or not.

    The time complexity for this algorithm is O(log(n)), where n is the input number.

    The worst case time complexity of this algorithm is given by the case of a non-happy number, since it gets stuck in
    a cycle, whereas a happy number quickly converges to 1. Let’s first calculate the time complexity of the Sum Digits
    function. Since we are calculating the sum of all digits in a number, the time complexity of this function is
    O(log(n)), because the number of digits in the number n log10n.


    Space complexity is O(1)

    Args:
        n (int): a positive integer
    Returns:
        bool: True if n is a happy number, False otherwise
    """

    def sum_of_squared_digits(number: int) -> int:
        """
        Helper function that calculates the sum of squared digits
        """
        total_sum = 0
        # an alternative
        # while number > 0:
        #     number, digit = divmod(number, 10)
        #     total_sum += digit ** 2
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum

    slow_pointer = n
    fast_pointer = sum_of_squared_digits(n)

    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    if fast_pointer == 1:
        return True

    return False
