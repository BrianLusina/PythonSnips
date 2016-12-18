def narcissistic(value):
    l = len(str(value))  # length of number
    return sum([pow(int(i), l) for i in str(value)]) == value
