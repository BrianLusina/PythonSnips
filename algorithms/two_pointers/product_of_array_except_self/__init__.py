from typing import List


def product_except_self_prefix_sums(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    result = [1] * len(nums)
    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


def product_except_self_two_pointers(nums: List[int]) -> List[int]:
    # Get the length of the input list
    n = len(nums)

    # Initialize a result list with 1's for products
    res = [1] * n

    # Initialize variables for left and right products
    left_product, right_product = 1, 1

    # Initialize pointers for the left and right ends of the list
    l = 0
    r = n - 1

    # Iterate through the list while moving the pointers towards each other
    while l < n and r > -1:
        # Update the result at the left index with the accumulated left product
        res[l] *= left_product

        # Update the result at the right index with the accumulated right product
        res[r] *= right_product

        # Update the left product with the current element's value
        left_product *= nums[l]

        # Update the right product with the current element's value
        right_product *= nums[r]

        # Move the left pointer to the right
        l += 1

        # Move the right pointer to the left
        r -= 1

    # Return the final product result list
    return res
