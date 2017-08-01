class Factorial(object):
    """
    class to obtain the factorial of a number
    """
    def __init__(self, number):
        self.number = number

    # provide a base case to exit and use recursion to obtain next number
    @staticmethod
    def fact(num):
        return 1 if num == 0 else num * Factorial.fact(num - 1)

