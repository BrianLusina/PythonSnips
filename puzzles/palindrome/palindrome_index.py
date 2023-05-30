def palindrome_index(word: str) -> int:
    word_length = len(word)
    first_pointer = 0
    last_pointer = word_length - 1

    while first_pointer < word_length:
        if word[first_pointer] != word[last_pointer]:
            break
        first_pointer += 1
        last_pointer -= 1

    # if the first pointer is at an index greater than the last pointer, then it means our string is a palindrome
    if first_pointer > last_pointer:
        return -1

    a = first_pointer + 1
    b = last_pointer

    while a < last_pointer and b > first_pointer + 1:
        if word[a] != word[b]:
            return last_pointer

        a += 1
        b -= 1


def palindrome_index_two(word: str) -> int:
    for i, j in enumerate(range(0, len(word) // 2), 1):
        if word[-i] == word[j]:
            continue
        if word[j:-i] == word[j:-i][::-1]:
            return len(word) - i
        elif word[j + 1:-i + 1] == word[j + 1:-i + 1][::-1]:
            return j
        return -1
    return -1
