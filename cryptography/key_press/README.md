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

Before predictive text entry systems like T9, you had to press a button repeatedly to cycle through the possible values
until you reached the one you wanted.

For example, to type "V8" you would press the 8 key three times and then again four times (pressing the 8 key cycles
through T->U->V->8), giving us a total of seven key presses.

Note: the 0 key handles spaces and outputs 0 when tapped twice.

Write a function that can calculate the amount of button presses required for any phrase. Except for spaces, punctuation
can be ignored. Your function should accept both uppercase and lowercase letters and treat them the same.

Examples:
presses('V8') # 7 presses('LOL') # 9 presses('How R u 2day') # 23

Bonus:  Try to avoid hard-coding the number of button presses for each letter!
Resource:  
Use python [Dictionaries](http://www.learnpython.org/en/Dictionaries) in this exercise



