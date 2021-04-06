def has_palindrome_permutation(some_string):
    # keep track of oddly appearing char
    unpaired_chars = set()

    for char in some_string:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    # the string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_chars) <= 1
