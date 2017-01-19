[![Build Status](https://travis-ci.org/BrianLusina/Python_Snippets.svg?branch=master)](https://travis-ci.org/BrianLusina/Python_Snippets)

[![codecov](https://codecov.io/gh/BrianLusina/Python_Snippets/branch/master/graph/badge.svg)](https://codecov.io/gh/BrianLusina/Python_Snippets)

15ea25bb8e9d461f9ec69a5fca3765d6

# Python Snippets
   
Repository for some of my simple [Python](https://www.python.org/ "Python") functions and snippets.
Each directory and/or python package has a readme for more information about the Python program

Clone the repo
```
git clone 

```

Activate a virtual env
```
virtualenv venv
```

or activate a virtual env with Python 3.+(this is recommended as most snippets run on Python3)
```
virtualenv -p python3 venv
```

install the requirements
```
pip install -r requirements.txt
```

**Enjoy!**
### Running tests

To run tests use `py.test`

``` sh
$ py.test tests
```
> This will run all the tests in the tests directory

To add tests, name your test folders `test_<MODULE_TO_TEST>.py`. This is to enable py.test to detect your tests.
Place these tests in the `tests` folder.

### Special file (documenter)

I call this special because it prints out the documentation for Python built in functions
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
Prints some Python built-in functions documents, such as abs(), int(), raw_input()

> Hint
The built-in document method is __doc__ is used
