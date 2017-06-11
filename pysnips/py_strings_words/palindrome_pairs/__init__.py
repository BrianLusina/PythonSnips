# todo: fix palindrome pairs
def palindrome_pairs(words):
    m = []
    for x in range(len(words)-1, 0, -1):
        for i in range(x):
            if is_palindrome(str(words[i]) + str(words[i+1])):
                w1 = words[i]
                w2 = words[i + 1]
                m.append([words.index(w1), words.index(w2)])
    return m


def is_palindrome(a):
    return str(a) == str(a)[::-1]

