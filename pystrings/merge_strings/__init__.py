def merge_alternately(word1: str, word2: str) -> str:
    word1_length = len(word1)
    word2_length = len(word2)

    if word1_length == 0:
        return word2

    if word2_length == 0:
        return word1

    merged_word = ""
    first_pointer = 0
    second_pointer = 0

    while first_pointer < word1_length or second_pointer < word2_length:
        if first_pointer < word1_length:
            merged_word += word1[first_pointer]
            first_pointer += 1

        if second_pointer < word2_length:
            merged_word += word2[second_pointer]
            second_pointer += 1

    return merged_word


def merge_alternately_2(word1: str, word2: str) -> str:
    word1_length = len(word1)
    word2_length = len(word2)

    merged_word = ""
    n = max(word1_length, word2_length)

    for x in range(n):
        if x < word1_length:
            merged_word += word1[x]
        if x < word2_length:
            merged_word += word2[x]

    return merged_word
