# from itertools import cycle, zip, count, islice


class FizzBuzz(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def simple_fizz(self):
        out = []
        for i in range(1, self.endpoint + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(i)
        return out

    """
    Using String concatenation
    """

    def string_concat(self):
        return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i for i in range(1, self.endpoint)]

    def string_concat_2(self):
        return [i % 3 // 2 * 'Fizz' + i % 5 // 4 * 'Buzz' or i + 1 for i in range(self.endpoint)]

    """
    You can also create a lazy, unbounded sequence by using generator expressions:
    """
    """
    def lazy(self):
        fizzes = cycle([""] * 2 + ["Fizz"])
        buzzes = cycle([""] * 4 + ["Buzz"])
        both = (f + b for f, b in izip(fizzes, buzzes))
        out = []
        # if the string is "", yield the number
        # otherwise yield the string
        fizzbuzz = (word or n for word, n in izip(both, count(1)))

        # print the first 100
        for i in islice(fizzbuzz, self.endpoint):
            out.append(i)
    """


"""
TESTS
Tests for the fizzbuzz challenges
"""
fizzy = FizzBuzz(10)
print(fizzy.simple_fizz())
