from typing import List


def count_bits(n: int) -> List[int]:
    """
    To understand the solution, we remember the following two points from math:

    All whole numbers can be represented by 2N (even) and 2N+1 (odd).
    For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when
    multiplying by ten in base 10).
    Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. Likewise,
    doubling a number and adding one will increase the count by exactly 1. Or:

    countBits(N) = countBits(2N)
    countBits(N)+1 = countBits(2N+1)

    Thus, we can see that any number will have the same bit count as half that number, with an extra one if it's an odd
    number. We iterate through the range of numbers and calculate each bit count successively in this manner:

        For i in range(num):
            counter[i] = counter[i // 2] + i % 2

    With a few modifications:

    - Define the base case of counter[0] = 0, and start at 1.
    - We need to include num, so use num+1 as the bound on the range.
    - Bit-shifting 1 has the same effect as dividing by 2, and is faster, so replace i // 2 with i >> 1.
    - We can choose to either initiate our list with counter = [0] * (num+1) or just counter = [0] and then append to it
    (which has O(1)). It's a little faster to initiate it with zeroes and then access it rather than appending each time,
    but I've chosen the latter for better readability.
    - Some solutions use i & 1 to determine the parity of i. While this accomplishes the same purpose as i % 2 and keeps
    with the bitwise-operator theme, it is faster to calculate the modulus.

    Time and Space Complexity
    Time: O(n) - We iterate through the range of numbers once.
    Space: O(n) - We use a num-sized array.

    Arguments:
        n (int): input number
    Returns:
        list: count of 1-bit in range up to n
    """
    counter = [0] * (n + 1)
    for i in range(1, n + 1):
        counter[i] = counter[i >> 1] + i % 2

    return counter
