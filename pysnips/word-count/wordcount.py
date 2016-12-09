# -*- coding: utf-8 -*-
from collections import Counter


def word_count(sentence):
    newsent = ''.join(map(lambda x: ' ' if not x.isalnum() else x, sentence))
    count = dict(Counter(newsent.lower().split()))
    return count
