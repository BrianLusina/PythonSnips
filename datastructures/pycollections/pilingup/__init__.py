for _ in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    length = len(lst)
    i = 0
    while i < length - 1 and lst[i] >= lst[i + 1]:
        i += 1
    while i < length - 1 and lst[i] <= lst[i + 1]:
        i += 1
    print("Yes" if i == length - 1 else "No")
