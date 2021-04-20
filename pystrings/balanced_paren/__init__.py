from typing import List, Generator


def balanced_parens(n: int) -> List[str]:
    """
    Returns a list of parenthesis
    :param n
    :returns list
    """
    return [x for x in generate_all_parens(n)]


def generate_all_parens(n: int) -> Generator:
    def compute_parens(left: int, right: int, s: str):
        if right == n:
            yield s
            return
        if left < n:
            yield from compute_parens(left + 1, right, s + "(")
        if right < left:
            yield from compute_parens(left, right + 1, s + ")")

    yield from compute_parens(0, 0, "")
