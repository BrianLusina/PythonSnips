def solve(arr, n):
    length_of_arr, count = len(arr), 0
    for i in range(length_of_arr):
        if arr[i] == 'D':
            for j in range(max(i - n, 0), min(i + n + 1, length_of_arr)):
                if arr[j] == 'C':
                    arr[j] = 0
                    count += 1
                    break
    return count


if __name__ == "__main__":
    print("Cats that can be caught", solve(['C', 'C', 'D', 'D', 'C', 'D'], 2))
