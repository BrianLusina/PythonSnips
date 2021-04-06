def cyclic_rotation(a: list, k: int) -> list:
    """
    Rotates an integers in array a by k number of times. Moving each element k positions to its right
    :param: a array of integers
    :param: k integer positions to move each element
    :returns: list of new integers moved k positions
    """

    length = len(a)

    if length == 0 or length == k or len(set(a)) == 1:
        return a

    output = [0 for _ in a]

    for index, value in enumerate(a):
        new_index = index + k

        if new_index >= length:
            new_position = new_index - length
            output[new_position] = value
        else:
            output[new_index] = value

    return output


def cyclic_rotation_2(nums: list, k: int) -> list:
    """
    This modifies the array nums in place though
    """
    length = len(nums)

    if length == 0:
        return nums

    k = k % length
    nums[:] = nums[length - k:] + nums[:length - k]
    return nums
