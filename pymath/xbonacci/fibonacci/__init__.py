def fib(a, b, end):
    c = 0
    fib_list = [a, b]
    if end == 0:
        return fib_list
    while c < end:
        nxt = fib_list[c] + fib_list[c + 1]
        fib_list.append(nxt)
        c += 1
        if nxt >= end:
            break
    return fib_list


def fib_memo(n):
    """
    uses memoization to reduce calculations by retrieving what has already been calculated
    :param n: number
    :return: resulting fibonacci
    """
    known = {0: 0, 1: 1}
    if n in known:
        return known[n]

    res = fib_memo(n - 1) + fib_memo(n - 2)
    known[n] = res
    return res


def nth_fibonacci(n):
    """
    Takes an integer n and returns the nth fibonacci
    :return: nth fibonacci
    """
    # edge cases
    if n < 0:
        raise Exception("Value in series can not be negative")
    elif n in [0, 1]:
        return n

    # we'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev_prev = 0  # 0th fibonacci
    prev = 1  # 1st fibonacci

    for _ in range(n - 1):
        # Iteration 1: current = 2nd fibonacci
        # Iteration 2: current = 3rd fibonacci
        # Iteration 3: current = 4th fibonacci
        # To get nth fibonacci ... do n-1 iterations.
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current
