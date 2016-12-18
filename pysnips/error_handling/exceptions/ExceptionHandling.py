try:
    print(7 / 0)
except ZeroDivisionError:
    print("Division by Zero will produce a black hole!")

try:
    print("Hello!")
    print("Nick" / 0)
except ZeroDivisionError:
    print("Someone divided something by zero")
except (ValueError, TypeError):
    print("You can't divide your name by zero!")

try:
    print("Hello!")
    print("Nick" / 0)
except:
    print("You can't divide your name by zero!")

try:
    print(800 / 0)
except ZeroDivisionError:
    print("Damn! divided by zero again! Quit that!")
finally:
    print("As I was saying, I think the black hole occurred when God divided infinite by zero. I'm just saying")


print("This is how the raise statement is used")
try:
    print(50 / 0)
except:
    print("Error Occured")
    raise

# statement is false, therefore will return an AssertionError
assert 5 * 2 == 12
temp = -29
assert (temp >= 0), "It's too damn cold!"
