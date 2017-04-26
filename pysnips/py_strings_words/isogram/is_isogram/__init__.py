def is_isogram(word):
    s = [c for c in word.lower() if c.isalpha()]
    return len(set(s)) == len(s)
