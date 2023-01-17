from typing import List


def find_capitals(word: str) -> List[int]:
    return [idx for idx, letter in enumerate(word) if letter.isupper()]
