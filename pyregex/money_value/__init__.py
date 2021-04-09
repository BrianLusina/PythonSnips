def money_value(s):
    is_neg = '-' in s
    result = "".join([x for x in s if x in "0123456789."])
    if result:
        result = float(''.join(result))
    else:
        result = 0.0
    if is_neg:
        result *= -1
    return result
