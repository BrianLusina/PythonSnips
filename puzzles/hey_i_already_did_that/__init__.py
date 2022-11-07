def hey_i_already_did_that(n: str, b: int) -> int:
    minion_ids = []

    while n not in minion_ids:
        minion_ids.append(n)
        n = get_next_minion_id(n, b)

    idx = minion_ids.index(n)

    if idx == len(minion_ids) - 1:
        return 1

    return len(minion_ids[idx:])


def get_next_minion_id(minion_id: str, base: int) -> str:
    k = len(minion_id)
    x = "".join(sorted(minion_id, reverse=True))
    y = "".join(sorted(minion_id))

    x_decimal = int(x, base)
    y_decimal = int(y, base)
    z_decimal = x_decimal - y_decimal

    z = decimal_to_base(z_decimal, base)

    while len(z) < k:
        z = "0" + z

    return z


def base_to_decimal(number: str, base: int) -> int:
    n = 0
    for digit in number:
        n = base * n + int(digit)
    return n


def decimal_to_base(number: int, base: int) -> str:
    if number < base:
        return str(number % base)
    digits = []
    while number >= base:
        rem = number % base
        digits.append(str(rem))
        number //= base

    if number > 0:
        digits.append(str(number))

    return "".join(digits)[::-1]
