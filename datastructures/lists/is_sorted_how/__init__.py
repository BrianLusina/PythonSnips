import operator
from itertools import islice


def is_sorted_and_how(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return 'yes, ascending'
    if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return 'yes, descending'
    else:
        return 'no'


def is_sorted_and_how_2(arr):
    return (
        'yes, ascending' if is_sorted_with(arr, operator.le) else
        'yes, descending' if is_sorted_with(arr, operator.ge) else
        'no')


def is_sorted_with(arr, pred):
    return all(pred(x, y) for x, y in zip(arr, islice(arr, 1, None)))
