"""
Create a list to store the fibonacci sequence numbers
add the first 2 numbers to the list, add them to get the third
create a counter variable to be used in the while loop, that will evaluate to false to avoid an infinite loop
This counter variable will also be used to iterate through the list adding consecutive numbers
break out of loop if next number is greater than end
"""
import unittest


def fib(a, b, end):
    c = 0
    fib_list = [a, b]
    if end == 0:
        return fib_list
    while c < end:
        nxt = fib_list[c] + fib_list[c+1]
        fib_list.append(nxt)
        c += 1
        if nxt >= end:
            break
    return fib_list

"""
TESTS
"""


class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(fib(0, 1, 1), [0, 1, 1])

    def test5(self):
        self.assertEqual(fib(5, 8, 89), [5, 8, 13, 21, 34, 55, 89])

    def test2(self):
        self.assertEquals(fib(0, 1, 34), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test3(self):
        self.assertEquals(fib(0, 1, 610), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])

    def test4(self):
        self.assertEquals(fib(5, 8, 144), [5, 8, 13, 21, 34, 55, 89, 144])
