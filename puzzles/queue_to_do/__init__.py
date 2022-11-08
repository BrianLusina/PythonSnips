def queue_to_do(start: int, length: int) -> int:
    if length == 1:
        return start
    val = get_xor(start + 2 * (length - 1))
    if start > 1:
        val = val ^ get_xor(start - 1)
    for i in range(length - 2):
        elems = length - 2 - i
        init = start + length * (2 + i) - 1
        val = val ^ get_xor(init + elems) ^ get_xor(init)
    return val


def get_xor(n):
    rem = n % 4
    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n + 1
    return 0
