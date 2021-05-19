from collections import Counter


def replacer(counter: Counter, word: str) -> str:
    for char, count in counter.items():
        for _ in range(count):
            if char.lower() in word.lower():
                i = word.lower().find(char.lower())
                letter = word[i]
                swapped = letter.swapcase()
                word = word.replace(letter, swapped)

    return word


# TODO: still failing tests
def work_on_strings(a: str, b: str) -> str:
    count_a = Counter(a.lower())
    count_b = Counter(b.lower())

    a = replacer(count_b, a)
    b = replacer(count_a, b)

    return a + b
