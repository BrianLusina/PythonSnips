from typing import List


def encode(words: List[str]) -> str:
    result = [f"{len(word)}#{word}" for word in words]
    return "".join(result)


def decode(encoded_str: str) -> List[str]:
    result, i = [], 0

    while i < len(encoded_str):
        j = i
        while encoded_str[j] != "#":
            j += 1
        word_length = int(encoded_str[i:j])
        word = encoded_str[j + 1:j + 1 + word_length]
        result.append(word)
        i = j + 1 + word_length

    return result
