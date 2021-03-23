def frequency(sentence):
    freq, out = {}, ""
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1

    return " ".join(["%s:%d" % (w, freq[w]) for w in sorted(freq)])
