## Caeser Cipher

have the function CaesarCipher(str, num) take the str parameter and perform a Caesar Cipher num on it using the num parameter as the numing number.
A Caesar Cipher works by numing all letters in the string N places down in the alphabetical order (in this case N will be num).
Punctuation, spaces, and capitalization should remain intact.
For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".
more on cipher visit [here](http://practicalcryptography.com/ciphers/caesar-cipher/)

## KEY PRESS

This is a feature phone keypad:
```

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |     | |     |
|  *  | |  0  | |  #  |
------- ------- -------

```
Before predictive text entry systems like T9, you had to press a button
repeatedly to cycle through the possible values until you reached
the one you wanted.

For example, to type "V8" you would press the 8 key three times and then
again four times (pressing the 8 key cycles through T->U->V->8),
giving us a total of seven key presses.

Note: the 0 key handles spaces and outputs 0 when tapped twice.

Write a function that can calculate the amount of button presses required for any phrase.
Except for spaces, punctuation can be ignored.
Your function should accept both uppercase and lowercase letters and treat them the same.

Examples:
presses('V8') # 7
presses('LOL') # 9
presses('How R u 2day') # 23

Bonus:  Try to avoid hard-coding the number of button presses for each letter!
Resource:  
Use python [Dictionaries](http://www.learnpython.org/en/Dictionaries) in this exercise

## Password


Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.


Hint:
use Python’s random module,

```
This is your first exposure to using Python code that somebody else wrote.
In Python, these formally-distributed code packages are called modules.
The thing we want from a module in this exercise is the ability to generate random numbers.
This comes from the random module.

To use a module, at the top of your file, type
```

```python
    import random
```
```
This means you are allowing your Python program to use a module called random in 
the rest of your code.

To use it (and generate a random integer), now type:
```
```python

    a = random.randint(2, 6)
```
Once you run this program, the variable a will have a random integer that the computer made for you, between 2 and 6 (including 2 and 6).
![Python Docs - Random module](https://docs.python.org/3.3/library/random.html)

Bonus:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

## Roman Numeral

Given a roman numeral as input, write a function that converts the roman numeral to a number and outputs it.
 Example:
```python 
translateRomanNumeral("LX") # 60
```

When a smaller numeral appears before a larger one, it becomes a subtractive operation. You can assume only one smaller numeral may appear in front of larger one.
Ex:
```python
translateRomanNumeral("IV") # 4
```
You should return `nil` on invalid input.

## Shell Game

"The Shell Game" involves three shells/cups/etc upturned on a playing surface, with a ball placed underneath one of them. The shells are then rapidly swapped round, and the game involves trying to track the swaps and, once they are complete, identifying the shell containing the ball.

This is usually a con, but you can assume this particular game is fair...

Your task is as follows. Given the shell that the ball starts under, and list of swaps, return the location of the ball at the end. All shells are indexed by the position they are in at the time.

For example, given the starting position 0 and the swap sequence [(0, 1), (1, 2), (1, 0)]:

The first swap moves the ball from 0 to 1
The second swap moves the ball from 1 to 2
The final swap doesn't affect the position of the ball.

So
```python
find_the_ball(0, [(0, 1), (2, 1), (0, 1)]) == 2
```
There aren't necessarily only three cups in this game, but there will be at least two. You can assume all swaps are valid, and involve two distinct indices.


## The Var

This should be fairly simple. It is more of a puzzle than a programming problem.
There will be a string input in this format: 'a+b' 2 lower case letters (a-z) seperated by a '+'
Return the sum of the two variables.
There is one correct answer for a pair of variables.
I know the answers, it is your task to find out.
Once you crack the code for one or two of the pairs, you will have the answer for the rest.
It is like when you were in school doing math and you saw "11 = c+h" and you needed to find out what c and h were.
However you don't have an 11. You have an unknown there as well. Example:
X = a+b.
You don't know what X is, and you don't know what b is or a, but it is a puzzle and you will find out.
As part of this puzzle, there is three hints or clues on solving this. I won't tell you what the other two are, but one of them is: Don't overthink it. It is a simple solution
Given the input as a string - Return the sum of the two variables as int.

## Maskify

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

"What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
