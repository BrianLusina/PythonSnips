"""
Finds the largest palindrome product of 2 n-digit nubers
"""


def find_largest_palindrome_product(n):
    """
    Finds the largest palindrome product of 2 n-digit numbers
    :param n: N digit number which specifies the number of digits of a given number
    :return: Largest Palindrome product of 2 n-digit numbers
    :rtype: int

    >>> find_largest_palindrome_product(2)
    9009
    """

    # first find the upper and lower limits for numbers with n digits
    upper_limit = 0

    for _ in range(1, n + 1):
        upper_limit *= 10
        upper_limit += 9

    # lower limit is 1 + the upper limit floor division of 10
    lower_limit = 1 + upper_limit // 10

    # initialize the max product
    max_product = 0

    for x in range(upper_limit, lower_limit - 1, -1):
        for y in range(x, lower_limit - 1, -1):
            product = x * y

            # short circuit early if the product is less than the max_product, no need to continue computation as this
            # already fails
            if product < max_product:
                break

            number_str = str(product)

            # check if this is a palindrome and is greater than the max_product currently
            if number_str == number_str[::-1] and product > max_product:
                max_product = product

    return max_product
