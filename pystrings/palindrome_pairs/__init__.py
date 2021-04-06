def palindrome_pairs(words):
    words = [str(word) for word in words]

    return [
        [i, j]
        for i, word_i in enumerate(words)
        for j, word_j in enumerate(words)
        if i != j and is_palindrome(word_i + word_j)
    ]


def is_palindrome(a):
    return str(a) == str(a)[::-1]
