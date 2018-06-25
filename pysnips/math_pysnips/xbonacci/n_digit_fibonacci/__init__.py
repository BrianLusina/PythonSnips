"""
Finds the first fibonacci number with n digits
"""


def n_digit_fibonacci(n):
    """
    Finds the index of the first fibonacci number with n digits
    An example:

    >>> n_digit_fibonacci(3)
    12

    :param n: number of digits to find for a fibonacci number
    :type n int
    :return: index of first fibonacci number with n digits
    :rtype: int
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"Expected n to be an integer and greater than 0, instead found {n}")

    # starting fibonacci sequence
    fib_list = [1, 1]

    # c is the counter(pointer) that will be used to find the next fibonacci number,
    # no_of_digits is the number of digits of the current fibonacci number
    # term is the term of the next fibonacci number, i.e. the current index in the fibonacci sequence of the sum of the
    # previous 2 fibonacci number in the sequence
    c = 0
    no_of_digits = 1
    term = 2

    while no_of_digits < n:

        # get the next fibonacci number
        fn = fib_list[c] + fib_list[c + 1]

        # get the number of digits
        fn_digits = len(str(fn))

        # if the length of the fibonacci number is greater than current number of digits, re-assign
        if fn_digits > no_of_digits:
            no_of_digits = fn_digits

        # add the fibonacci number
        fib_list.append(fn)

        # increase the term and counter
        c += 1
        term += 1

    return term


if __name__ == "__main__":
    digits = 1000
    number = n_digit_fibonacci(digits)
    print(f"Index of the first fibonacci number with {digits} digits is {number}")
