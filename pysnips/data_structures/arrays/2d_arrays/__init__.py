import os


def hour_glass_sum(array):
    max_sum = None

    for x in range(4):
        for y in range(4):
            hour_glass = sum(array[x][y:y + 3]) + sum(array[x + 2][y:y + 3]) + array[x + 1][y + 1]

            if max_sum is None or max_sum < hour_glass:
                max_sum = hour_glass
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hour_glass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
