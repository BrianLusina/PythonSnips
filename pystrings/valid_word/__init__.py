from typing import List


def valid_word(seq: List[str], word: str) -> bool:
    for s in sorted(seq):
        word = word.replace(s, "")

    return len(word) == 0
