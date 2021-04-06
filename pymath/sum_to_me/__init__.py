n = int(input("Enter a number: "))


def sum_me(n):
    total = 0.0
    for i in range(1, n + 1):
        total += float(float(i) / (i + 1))
    return total


print(sum_me(n))
