def cake_is_not_a_lie(s: str) -> int:
    str_len = len(s)
    for x in range(1, str_len + 1):
        part = s[:x]
        count = s.count(part)
        if count * x == str_len:
            return count
    else:
        return 0
