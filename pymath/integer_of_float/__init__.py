def i_or_f(arr):
    try:
        return isinstance(float(arr), float) or isinstance(int(arr), int)
    except ValueError:
        return False
