def digit_sum(n):
    #function to sum all the digits of a number
    #convert the number into a string
    stringConvert = str(n)
    total = 0
    #loop through each string and convert it into an integer
    for i in stringConvert:
        x = int(i)
        total += x
    #return the total
    return total

def factorial(x):
    #function that returns the factorial of a non-negative number
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

def is_prime(x):
    if x < 2:
        return False
    for n in range(2, (x-1)):
        if x % n == 0:
            return False    
    else:
        return True

def reverse(text):
    #function to reverse text in a string e.g abc becomes cba
    rev= ""
    count=1
    #for i in range(len(text)):
    while count <= len(text):
         rev += text[len(text)-count]
         count+=1
    return rev        

def anti_vowel(text):
	#function to remove all vowels from a text
    vowels={'a','e','i','o','u','A','E','I','O','U'}
    vtext=''.join(letter for letter in text if letter not in vowels)
    return vtext

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
    found = 0
    for n in sequence:
        if n == item:
            found += 1
    return found


"""takes in a list of numbers, removes all odd numbers in the list, and returns the result."""
def purify(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result


"""returns the product of all the items in a list"""
def product(l):
    result = 1
    for i in l:
         result = result * i
    return result


"""that takes in a list and removes elements of the list that are the same."""
def remove_duplicates(myList):
    return list(set(myList))


"""func to find median in a list"""
def median(lst):
    sortList = sorted(lst)
    med = 0
    if len(sortList) == 1:
        med = sortList[0]
    elif len(sortList)%2 == 0:
        fMidIndex = len(sortList)/2
        sMidIndex = fMidIndex - 1
        med = (sortList[fMidIndex] + sortList[sMidIndex]) / 2.0
    elif len(sortList)%2 != 0:
        fMidIndex = (len(sortList)/2)
        med = sortList[fMidIndex]
    return med    