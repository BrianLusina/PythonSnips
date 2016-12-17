class ListToTuple(object):
    """
    Splits the user input into a list with commas as separators
    converts the list into a tuple and returns it
    """
    def __init__(self, user_input):
        self.user_input = user_input

    def converter(self):
        lst = self.user_input.split(",")
        return tuple(lst)

user_input = input("Please enter a list of numbers")
conv = ListToTuple(user_input)
print(conv.converter())
