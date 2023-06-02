def gcd_of_strings_brute_force(str1: str, str2: str) -> str:
    len_1, len_2 = len(str1), len(str2)

    def valid(k: int):
        if len_1 % k or len_2 % k:
            return False

        n1, n2 = len_1 // k, len_2 // k
        base = str1[:k]

        return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len_1, len_2), 0, -1):
        if valid(i):
            return str1[:i]

    return ""


def gcd_of_strings_(str1: str, str2: str) -> str:
    pass
