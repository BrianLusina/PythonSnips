# Write a function that return whether or not the input string has balanced parantheses
# Balanced:
#   '((()))'
#   '(()())'
#2 Not balanced:
#   '((()'
#   '())('

import unittest


def count(paren):
    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in paren:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False
    return not len(stack)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, count('((()))'))

    def test2(self):
        self.assertEqual(True, count('(()())'))

    def test3(self):
        self.assertEqual(False, count('((()'))

    def test4(self):
        self.assertEqual(False, count('())('))
