"""Longest word in a sentence"""
def find_longest(string):
    spl = string.split()
    numberList = []
    for i in spl:
        numberList.append(len(i))
    return max(numberList)