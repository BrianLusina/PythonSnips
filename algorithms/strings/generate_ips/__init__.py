from typing import List

from ..validate_ip import is_valid_ipv4


def backtrack(s: str, current: List[str], start: int, ips: List[str]):
    if len(current) == 4:
        if start == len(s):
            ips.append(".".join(current))
        return
    for i in range(start, min(start + 3, len(s))):
        if s[start] == '0' and i > start:
            continue
        if 0 <= int(s[start:i + 1]) <= 255:
            backtrack(s, current + [s[start:i + 1]], i + 1, ips)


def gen_ips(s: str) -> List[str]:
    ips = []
    backtrack(s, [], 0, ips)
    return ips


def generate_ip(s: str) -> List[str]:
    """
    Time Complexity: O(n^3), where n is the length of the string
        Three nested traversal of the string is needed, where n is always less than 12.
    Auxiliary Space: O(n).
        As as extra space is needed.
    @param s:
    @return:
    """
    size = len(s)

    if size > 12:
        return []

    s_new = s
    ips = []

    # generate different combinations
    for x in range(1, size - 2):
        for y in range(x + 1, size - 1):
            for z in range(y + 1, size):
                s_new = f"{s_new[:z]}.{s_new[z:]}"
                s_new = f"{s_new[:y]}.{s_new[y:]}"
                s_new = f"{s_new[:x]}.{s_new[x:]}"

                if is_valid_ipv4(s_new):
                    ips.append(s_new)

                s_new = s

    return ips
