"""Exception Handling is done using try/except syntax. The try block handles the code that may contain an error
when it occurs, while the Except block handles the code that is run when the try block encounters an error

    try:
        code to run
    except ErrorType:
        code is run when an error is encountered
"""
try:
    print (7/0)
except ZeroDivisionError:
    print("Division by Zero will produce a black hole!")

"""
The Except block can handle multiple errors as well
    try:
        code
    except  ErrorType:
        code
    except (ErrorType1,ErrorType2):
        code

"""
try:
    print("Hello!")
    print("Nick"/0)
except ZeroDivisionError:
    print("Someone divided something by zero")
except (ValueError,TypeError):
    print ("You can't divide your name by zero!")

"""
    Alternatively, This will catch all errors, but programmer will never know which exact error occured, thus should
    be used sparingly
        try:
            code
        except:
            code
"""
try:
    print("Hello!")
    print("Nick"/0)
except:
    print ("You can't divide your name by zero!")

"""
finally statement shall run no matter what error occurs. Placed at the bottom of the try/except block
    try:
        code
    except ErrorType:
        code
    finally
        code
"""
try:
    print(800/0)
except ZeroDivisionError:
    print("Damn! divided by zero again! Quit that!")
finally:
    print("As I was saying, I think the black hole occured when God divided infinite by zero. I'm just saying")

"""
raise statement is used to "raise" an exception. raise ErrorType. The exception has to be specified
The raise statement can "raise" exceptions with arguments containing details about them
    raise ErrorType(args)
The raise statement can also be used in an except block to re-raise any exceptions that occured
        try:
            code
        except:
            code
            raise
"""

print ("This is how the raise statement is used")
try:
    print (50/0)
except:
    print("Error Occured")
    raise

"""
Assertion is a sanity check that is used to test programs. The assert statement is used on a statement and if statement
is false, it will raise an AssertionError
    assert statement

assert can take a second argument detailing the AssertionError raised
    temp = -29
    assert (temp>=0), "It's too damn cold!"
"""
#statement is false, therefore will return an AssertionError
assert 5*2 == 12
temp = -29
assert (temp >= 0), "It's too damn cold!"
