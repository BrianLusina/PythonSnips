# String Manipulation

Series of problems and solutions to String manipulation in Python. Of course there are dozens of other ways to solve these problems.
Here is a breakdown of challenges and their descriptions

## Denumerate String
You have to rebuild a string from an enumerated list.

the function only accepts a list of tuples where each tuple consists of 2 elements
the first element of the tuple will be the index of the reconstructed string and the second element a single alphanumeric character
the indexes must start from zero and must match with how indexes are numbered normally, so gaps between indexes are not allowed
tuples don't have to be ordered by the indexes
The function should return False otherwise.

Input example:

[(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]
Returns
'monty'

## Count vegetables

Help Suzuki count his vegetables....

Suzuki is the master monk of his monastery so it is up to him to ensure the kitchen is operating at full capacity to feed his students and the villagers that come for lunch on a daily basis.

This week there was a problem with his deliveries and all the vegetables became mixed up. There are two important aspects of cooking in his kitchen, it must be done in harmony and nothing can be wasted. Since the monks are a record keeping people the first order of business is to sort the mixed up vegetables and then count them to ensure there is enough to feed all the students and villagers.

You will be given a string with the following vegetables:

"cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"
Return a list of tuples with the count of each vegetable in descending order. If there are any non vegetables mixed in discard them. If the count of two vegetables is the same sort in descending alphabetical order.
``` python
(119, "pepper"),
(114, "carrot"),
(113, "turnip"),
(102, "onion"),
(101, "tofu"),
(100, "cabbage"),
(93, "mushroom"),
(90, "cucumber"),
(88, "potato"),
(80, "celery")
```

## ReOrdering

There is a sentence which has a mistake in it's ordering.

The part with a capital letter should be the first word.

Please build a function for re-ordering

Examples
``` python
>>> re_ordering('ming Yao')
'Yao ming'

>>> re_ordering('Mano donowana')
'Mano donowana'

>>> re_ordering('wario LoBan hello')
'LoBan wario hello'

>>> re_ordering('bull color pig Patrick')
'Patrick bull color pig'
```

## Correct The Time String

A very easy task for you!

You have to create a method, that corrects a given time string. There was a problem in addition, so many of the time strings are broken. Time-Format is european. So from "00:00:00" to "23:59:59". 

Some examples:

"09:10:01" -> "09:10:01"
"11:70:10" -> "12:10:10"
"19:99:99" -> "20:40:39"
"24:01:01" -> "00:01:01"

If the input-string is null or empty return exactly this value! (empty string for C++)
If the time-string-format is invalid, return null. (empty string for C++)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.

## Your order Please

Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

## isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

```python
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```

## Chromosome Check

The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";

##Time Degrees

Note : Please use python 3.4.3 , there is round off issue that is being resolved with python 2.7 , THANKS !

Time , time , time . Your task is to write a function that will return the degrees on a analog clock from a digital time that is passed in as parameter . The digital time is type string and will be in the format 00:00 . You also need to return the degrees on the analog clock in type string and format 360:360 . Remember to round of the degrees . Remeber the basic time rules and format like 24:00 = 00:00 and 12:60 = 13:00 . Create your own validation that should return "Check your time !" in any case the time is incorrect or the format is wrong , remember this includes passing in negatives times like "-01:-10".

A few examples :
```python
clock_degree("00:00") will return : "360:360"
clock_degree("01:01") will return : "30:6"
clock_degree("00:01") will return : "360:6"
clock_degree("01:00") will return : "30:360"
clock_degree("01:30") will return : "30:180"
clock_degree("24:00") will return : "Check your time !"
clock_degree("13:60") will return : "Check your time !"
clock_degree("20:34") will return : "240:204"
```
Remember that discrete hour hand movement is required - snapping to each hour position and also coterminal angles are not allowed. Goodluck and Enjoy !

## Complete The Pattern

You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows.

Note:Returning the pattern is not the same as Printing the pattern.
Rules/Note:

If n < 1 then it should return "" i.e. empty string.
There are no whitespaces in the pattern.
Pattern:
1

22
333
....
.....
nnnnnn
Examples:

```python
pattern(5):

1
22
333
4444
55555
pattern(11):

1
22
333
4444
55555
666666
7777777
88888888
999999999
10101010101010101010
1111111111111111111111
```
* Hint: Use \n in string to jump to next line

Tags
> PUZZLES LOOPS CONTROL FLOW BASIC LANGUAGE FEATURES FUNDAMENTALS SEQUENCES ARRAYS STRINGS

## Name That Number

In this kata, you'll be given an integer of range 0 <= x <= 99 and have to return that number spelt out in English. A few examples:

```python
name_that_number(4)   # returns "four"
name_that_number(19)  # returns "nineteen"
name_that_number(99)  # returns "ninety nine"
```

Words should be seperated by only spaces and not hyphens. No need to validate parameters, they will always be in the range [0, 99]. Make sure that the returned String has no leading of trailing spaces. Good luck!

## Swappie

Using python, have the function SwapCase(str) take the str parameter and swap the case of each character.
For example: if str is "Hello World" the output should be hELLO wORLD.
Let numbers and symbols stay the way they are.

NB do not use the swapcase python method.

## reverse

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

## AntiVowel

Remove all vowels from a text

## Scrabble Score

Function that takes word input and returns equivalent scrabble score

## Censor

Function that takes a word,searches for it in text and replaces it with asterisks similar in number to the length of the word

## Longest Word

Find the Longest word in a sentence

## Name Score

The 26 letters of the English alphabets are randomly divided into 5 groups of 5 letters with the remaining letter being ignored. Each of the group is assigned a score of more than 0. The ignored letter always has a score of 0.

With this kata, write a function nameScore(name) to work out the score of a name that is passed to the function.

The output should be returned as an object:

{'Mary Jane':20}
Only letters have a score. Spaces do not.

You can safely assume that name does not contain any punctuations or symbols. There will also be no empty string or null value.

A static alpha object for testing has been preloaded for your convenience in the following format:

{'ABCDE':1,'FGHIJ':2,'KLMNO':3,'PQRST':4,'UVWXY':5}  //'Z' is ignored
Note that the alpha object will be randomly generated each time you run the test.

Example

In accordance to the above alpha object, the name Mary Jane will have a name score of 20 => M=3 + a=1 + r=4 + y=5 + J=2 + a=1 + n=3 + e=1

## Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.
As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
If the length of the input string is 0, return value must be 0.
Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

## Pangram Checker

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Alternatively

## Accum

This time no story, no theory. The examples below show you how to write function accum:

Examples:
``` python
accum("abcd") --> "A-Bb-Ccc-Dddd"
accum("RqaEzty") --> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") --> "C-Ww-Aaa-Tttt"
```

> The parameter of accum is a string which includes only letters from a..z and A..Z.


## Wrong End

You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!

Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics - simples!

## XOXO

being passed and return the string true if there is an equal number of x's and o's,
because you cannot recieve an uneven number of hugs and kisses :-)
otherwise return the string false. Only these two letters will be entered in the string,
no punctuation or numbers.
For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

## Paren Matcher

Write a function that return whether or not the input string has balanced parantheses
Balanced:
'((()))'
'(()())'

2 Not balanced:
'((()'
'())('

## Zebulans Nightmare

Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

``` python
zebulansNightmare('camel_case') == 'camelCase'
zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
zebulansNightmare('get_string') == 'getString'
zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
zebulansNightmare('main') == 'main'
```


## Father Son

This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version
Task:
Every uppercase letter is Father, The corresponding lowercase letters is the Son.
Give you a string s, If the father and son both exist, keep them.
If it is a separate existence, delete them. Return the result.
For example:
``` python
sc("Aab") should return "Aa"
sc("AabBc") should return "AabB"
sc("AaaaAaab") should return "AaaaAaa"(father can have a lot of son)
sc("aAAAaAAb") should return "aAAAaAA"(son also can have a lot of father ;-)
```


## LineUp Students

Suzuki needs help lining up his students!

Today Suzuki will be interviewing his students to ensure they are progressing in their training. He decided to schedule the interviews based on the length of the students name in descending order. The students will line up and wait for their turn.

You will be given a string of student names. Sort them and return a list of names in descending order.

Here is an example input:

string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
Here is an example return from your function:

 lst = ['Takehiko',
        'Takayuki',
        'Takahiro',
        'Takeshi',
        'Takeshi',
        'Takashi',
        'Tadashi',
        'Takeo',
        'Takao']
Names of equal length will be returned in descending alphabetical order such that:

string = "xxa xxb xxc xxd xa xb xc xd"
Returns

['xxd', 'xxc', 'xxb', 'xxa', 'xd', 'xc', 'xb', 'xa']


## Remove Duplicates and Sort

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
```python
hello world and practice makes perfect and hello world again
```
Then, the output should be:
```python
again and hello makes perfect practice world
```

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

## Duplicate Encoder

The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:
``` python
"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("
```
Tags
> FUNDAMENTALS STRINGS ARRAYS

## Letter Digit Count

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
