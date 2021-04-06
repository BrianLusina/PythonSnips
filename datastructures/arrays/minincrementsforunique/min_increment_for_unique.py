def minIncrementForUnique(A: list) -> int:
    if len(A) == 0:
        return 0

    A.sort()

    previous = A[0]
    min_increments = 0

    for i in range(1, len(A)):
        if A[i] <= previous:
            temp = A[i]
            A[i] = previous
            A[i] += 1
            min_increments += A[i] - temp
        previous = A[i]

    return min_increments
