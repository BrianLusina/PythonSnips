def binary_converter(number):
    try:
        return "{0:b}".format(number) if number in range(0, 256) else "Invalid input"
    except TypeError:
        return "Invalid input"
