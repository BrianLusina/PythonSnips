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
