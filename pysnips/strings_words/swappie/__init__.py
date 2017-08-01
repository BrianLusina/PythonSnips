class Swap(object):
    def __init__(self, str_input):
        self.str_input = str_input

    # simple solution
    def swappie(self):
        print("Using for loop")
        out = ""
        for x in self.str_input:
            if x.islower():
                out += x.upper()
            else:
                out += x.lower()
        return out

    # alternative solution using inbuilt
    def swappie_two(self):
        print("Using inbuilt function swapcase()")
        return self.str_input.swapcase()

    # using map
    def swappie_three(self):
        print("Using map function and inbuilt function")
        return "".join(map(str.swapcase, self.str_input))

    # using lambda
    def swappie_four(self):
        print("using lambda function")
        m = lambda x: x.lower() if x.isupper() else x.upper()
        return m(self.str_input)
