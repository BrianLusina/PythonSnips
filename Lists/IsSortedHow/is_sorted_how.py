def is_sorted_and_how(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return 'yes, ascending'
    if all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return 'yes, descending'
    else:
        return 'no'

