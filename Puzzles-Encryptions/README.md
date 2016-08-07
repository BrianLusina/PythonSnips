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
