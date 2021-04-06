def truncate_string(sentence, n):
    if n <= 3:
        return sentence[0: n] + "..."
    if len(sentence) > n:
        return sentence[0:n - 3] + "..."
    else:
        return sentence
