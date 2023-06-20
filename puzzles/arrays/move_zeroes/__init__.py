from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Modifies the list in place by moving the non-zero elements to the front maintaining their order and the zero elements
    to the back. This uses 2 pointers with the left & right pointers being initialized at 0 and checking the value of
    each pointer at each iteration. It performs a swap of the values if the left and right pointers are at elements
    that are 0 and non-zero respectively, This way, non-zero elements retain their order, while 0 elements are moved to
    the back.

    Complexity:

    Time Complexity: O(n) as we traverse the entire list checking for non-zero elements and perform a swap with 0 elements
    from the previous position.

    Space Complexity: O(1), only constant extra space is used, as there is no additional list used to store the elements
    """
    if len(nums) == 1:
        return

    left_pointer = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[left_pointer], nums[current] = nums[current], nums[left_pointer]
            left_pointer += 1


def move_zeroes_one(nums: List[int]) -> None:
    """
    Moves zero elements to the back while maintaining the order or non-zero elements. This counts the number of 0 elements
    in the list which is an O(n) operation where n is the size of the list, as it traverses the list from beginning to end

    Then creates an intermediate list which will contain all the non-zero elements from the original list in the same order
    This is done by traversing the list and adding the non-zero elements to the intermediate list. This can be done in the
    same loop as the above operation, but will still be an O(n) operation. The Space complexity will be O(n) as the non-zero
    elements are stored in a separate list.

    Now, the zero elements are moved to the end of the intermediate list.

    Finally, we combine the result by modifying the initial list with the intermediate list

    Complexity:
    Time: O(n)
    Space: O(n)
    """
    if len(nums) == 1:
        return

    number_of_zeroes = 0
    intermediate: List[int] = []

    for num in nums:
        if num == 0:
            number_of_zeroes += 1
        else:
            intermediate.append(num)

    while number_of_zeroes:
        intermediate.append(0)
        number_of_zeroes -= 1

    for x in range(len(nums)):
        nums[x] = intermediate[x]
