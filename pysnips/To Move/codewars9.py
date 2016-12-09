from math import sqrt
#function to get the next perfect square
def find_next_square(sq):
    return (sqrt(sq)+1)**2 if sqrt(sq).is_integer == True else -1

#function to get the count of both vowels and consonants
def get_count(words=""):
    if not isinstance(words, str):
        return {'vowels':0,'consonants':0}
    letter = "".join([c.lower() for c in words if c.isalpha()])
    vowel = "".join([c for c in letter if c in 'aeiou'])
    consonant = "".join([c for c in letter if c not in 'aeiou']) 
    return {'vowels':len(vowel),'consonants':len(consonant)}

"""Description:
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input
Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.
Example Input
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.
Example Output
["Open", "Open", "Senior", "Open", "Open", "Senior"]"""
def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]

"""
You are asked to write a myParseInt method with the following rules:

It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
For all other strings (including the ones representing float values), it should return NaN
It should assume that all numbers are not signed and written in base 10
"""
def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 'NaN'

"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
"""
def likes(names):
	count = 0
	if len(names) == 0 :
		return "no one likes this"
	elif len(names) ==1:
		return names[0] + " likes this"
	elif len(names) == 2:
		return names[0] + " and " + names[1] + " like this"
	elif len(names) == 3:
		return names[0] + ", " + names[1] + " and  "+ names[2] + " like this"
	elif len(names) > 3:
		return names[0] + ", " + names[1] + " and  "+ str(len(names)-2) + " others like this"

"""Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!"."""
def disemvowel(string):
    vow = b'aeiouAEIOU'
    return string.translate(None,vow)

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse(s[:-1])

