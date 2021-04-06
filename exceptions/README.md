Sample Error Handling in Python

Exception Handling is done using try/except syntax. The try block handles the code that may contain an error when it
occurs, while the Except block handles the code that is run when the try block encounters an error

``` python
try:
    code to run
except ErrorType:
    code is run when an error is encountered
```

The Except block can handle multiple errors as well

``` python
try:
    code
except  ErrorType:
    code
except (ErrorType1,ErrorType2):
    code
```

Alternatively, This will catch all errors, but programmer will never know which exact error occured, thus should be used
sparingly

``` python
try:
    code
except:
    code
``` 

finally statement shall run no matter what error occurs. Placed at the bottom of the try/except block

``` python    
try:
    code
except ErrorType:
    code
finally
    code
```

raise statement is used to "raise" an exception.

``` python
raise ErrorType.
```

The exception has to be specified The raise statement can "raise" exceptions with arguments containing details about
them

``` python
raise ErrorType(args)
```

The raise statement can also be used in an except block to re-raise any exceptions that occured

``` python
try:
    code
except:
    code
    raise
```

Assertion is a sanity check that is used to test programs. The assert statement is used on a statement and if statement
is false, it will raise an AssertionError

``` python
assert statement
```

assert can take a second argument detailing the AssertionError raised

``` python
temp = -29
assert (temp>=0), "It's too damn cold!"
```
