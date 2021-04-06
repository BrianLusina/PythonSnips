def compute_sum(n):
    return sum(int(c) for i in range(n + 1) for c in str(i))
