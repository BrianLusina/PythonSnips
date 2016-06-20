"""
function that takes in a number string and finds the highest and lowest values and outputs the string result with the highes preceding
"""
def high_and_low(numbers):
	li,count = [],0
	numbers = numbers.split()
	while count < len(numbers):
		for i in numbers:
			li.append(int(i))
			maxNminN = str(max(li)) + " " + str(min(li))
		return maxNminN
	count+=1

"""
Write a function to return a string containing all except the first and last characters, separated by spaces. If the input string is empty, or the removal of the first and last items would cause the string to be empty, return null.

Arrays are joined by adding a single space between each consecutive array element.
"""
def array(string):
	s,r = string.replace(","," ").replace(" ",""),""
	if len(s) < 3:
		return None
	else:
		li = list(s)
		del(li[0])
		del(li[len(li)-1])
		for i in li:
		    r += i
		return " ".join(r)
		#alternatively
def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None

"""Function reverses a string and maintains the order of the words reverese in the string"""
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))        

"""
Description:

Your task is to make a function that can take any non-negative integer as a argument and return it with it's digits in descending order. Descending order means that you take the highest digit and place the next highest digit immediately after it.

Examples:

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221

"""
def Descending_Order(num):
    return int("".join(sorted(list(str(num)),key=int,reverse = True)))        

