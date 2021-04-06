from collections import Counter
from string import ascii_lowercase


def closeStrings(self, word1: str, word2: str) -> bool:
    """
    Operation 1 allows us to swap any two symbols, so what matters in the end is not the order of them, but how many of each symbol we have. 
    Imagine we have (6, 3, 3, 5, 6, 6) frequencies of symbols, than we need to have the same frequencies for the second string as well. 
    So, we need to check if we have the same elements, but in different order (that is one is anagramm of another). We can do it in 2 ways. 
    We can sort both of them and compare, or we can use Counter again to check if these two lists have the same elements.
    
    Operation 2 allows us to rename our letters, but we need to use the same letters: it means, that set of letters in first and second strings should be the same.
    """
    if len(word1) != len(word2):
        return False

    counts_1 = Counter(word1)
    counts_2 = Counter(word2)

    return set(word1) == set(word2) and Counter(counts_1.values()) == Counter(counts_2.values())


def closeStrings2(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    alpha = ascii_lowercase
    counts1 = []
    counts2 = []
    for char in alpha:
        in1, in2 = char in word1, char in word2
        if in1 and in2:
            counts1.append(word1.count(char))
            counts2.append(word2.count(char))
        elif (in2 and not in1) or (in1 and not in2):
            return False
    counts2.sort()
    counts1.sort()
    return counts1 == counts2
