class InputOutString(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Input a string: ")

    def print_string(self):
        return self.s.upper()

cl = InputOutString()
print(cl.get_string())
print(cl.print_string())
