## Password

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method.

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

Once you run this program, the variable a will have a random integer that the computer made for you, between 2 and 6 (
including 2 and 6).
![Python Docs - Random module](https://docs.python.org/3.3/library/random.html)

Bonus:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.