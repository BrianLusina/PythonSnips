def frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    words = freq.keys()
    sorted(words)

    for w in words:
        print("%s:%d" % (w,freq[w]))