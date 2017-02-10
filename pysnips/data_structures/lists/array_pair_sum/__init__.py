def array_pair_sum(k, array):
    """
    Iterative method
    Loops through the array, checking if a pair sums up to the value k
    Returns all pairs that sum up to k
    complexity: O(n^2)
    :param k: The value to check sum of pairs against
    :param array: The array of integers to loop through
    :return: The sum of pairs
    :rtype: list
    """
    result = []
    for x in range(len(array)):
        for y in range(x + 1, len(array)):
            if array[x] + array[y] == k:
                result.append([array[x], array[y]])

    return result


def array_pair_sum_sort(k, arr):
    """
    first sort the array and then use binary search to find pairs.
    complexity: O(nlogn)
    """

    result = []
    arr.sort()

    for i in range(len(arr)):
        if k - arr[i] in arr[i + 1:]:
            result.append([arr[i], k - arr[i]])

    return result


def array_pair_sum_hash_table(k, arr):
    """
    Use a hash table to store array elements of pairs.
    complexity: O(n)
    """

    result = []
    hash_table = {}

    for e in arr:
        if e in hash_table:
            result.append([k - e, e])
        else:
            hash_table[k - e] = True
    result.reverse()

    return result
