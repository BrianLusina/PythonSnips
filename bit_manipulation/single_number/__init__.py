from typing import List
from functools import reduce


def single_number(nums: List[int]) -> int:
    """Finds the single number that has not been duplicated.

    If we take XOR of a number and a zero, the result will be that number, i.e. a⊕0=a.
    If we take XOR of two same numbers, it will return 0, i.e. a⊕a=0.
    If we take XOR of multiple numbers, the order doesn't affect the result, i.e. a⊕b⊕c=a⊕c⊕b.

    Therefore, if we take XOR of all numbers, what's left would be that single number as every element that appears
    twice would be cancelled out. For example, nums=[4,1,2,1,2], we can reorder it like [1,1,2,2,4], and we got
    (1⊕1)⊕(2⊕2)⊕4=4.
    """
    return reduce(lambda x, y: x ^ y, nums)


def single_number_math(nums: List[int]) -> int:
    """
    Finds the single number that has not been duplicated.
    2∗sumOfSet−(SumOfNumbers)=answer

    For example, nums=[4,1,2,1,2], sumOfSet is 1+2+4=7 and sumOfNumbers is 1+1+2+2+4=10. Then the answer is 2∗7−10=4.

    >>> single_number_math([4,1,2,1,2])
    >>> 4
    """
    hash_set = set(nums)
    sum_of_set = sum(hash_set)
    sum_of_nums = sum(nums)
    return 2 * sum_of_set - sum_of_nums
