def multiply(n):
    return 5 ** len(str(n)) * n if n > 1 else (5 ** (len(str(n)) - 1)) * n
