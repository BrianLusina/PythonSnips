from typing import Union


def calculate_partial_result(prev_char: str, count: int) -> str:
    return prev_char + (str(count) if count > 1 else '')


def compress(s: str) -> Union[None, str]:
    if not s or s is None:
        return s

    prev_char = s[0]
    count = 0
    result = ''

    for char in s:
        if char == prev_char:
            count += 1
        else:
            result += calculate_partial_result(prev_char, count)
            prev_char = char
            count = 1

    result += calculate_partial_result(prev_char, count)
    return result if len(result) < len(s) else s
