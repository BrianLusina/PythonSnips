def digit_sum(n):
    # function to sum all the digits of a number
    # convert the number into a string
    stringConvert = str(n)
    return sum([int(i) for i in stringConvert])



score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
"""funct that takes word input and returns equivalent scrabble score"""
def scrabble_score(word):
    #change all letters to lower
    word = word.lower()
    total = 0
    for letter in word:
        total += score[letter]
    return total


"""Function that takes a word,searches for it in text and replaces it with asterisks similar in number to the length of the word"""
def censor(text,word):
    stringList = text.split()
    newList = []
    newSent = ""
    for w in stringList:
        if w == word:
            newList.append("*" * len(word))
        else:
            newList.append(w)

        newSent = " ".join(newList)
    return newSent


"""Function that counts the number of times an item appears in a list"""
def count(sequence,item):
    m = [n for n in sequence if n == item]
    return len(m)


"""takes in a list of numbers, removes all odd numbers in the list, and returns the result."""
def purify(l):
    return [i for i in l if i % 2 == 0]


"""returns the product of all the items in a list"""
def product(l):
    result = 1
    for i in l:
         result = result * i
    return result


"""that takes in a list and removes elements of the list that are the same."""
def remove_duplicates(myList):
    return list(set(myList))
