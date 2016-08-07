def digit_sum(n):
    # function to sum all the digits of a number
    # convert the number into a string
    stringConvert = str(n)
    return sum([int(i) for i in stringConvert])


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
