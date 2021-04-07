from bisect import insort


def find_median(arr):
    """
    Finds the median of an array.
    """
    len_of_list = len(arr)

    if len_of_list % 2 == 0:
        l = arr[len_of_list // 2]
        r = arr[(len_of_list // 2) - 1]
        return (l + r) / 2.0
    elif len_of_list % 2 != 0:
        return float(arr[len_of_list // 2])


n = int(input().strip())
heap = []
for _ in range(n):
    x = int(input().strip())
    insort(heap, x)
    print(find_median(heap))
