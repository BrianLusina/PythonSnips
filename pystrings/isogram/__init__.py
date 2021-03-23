def is_isogram(word):
    if word is None or not isinstance(word, str):
        return False
    s = [c for c in word.lower() if c.isalpha()]
    return len(set(s)) == len(s)
