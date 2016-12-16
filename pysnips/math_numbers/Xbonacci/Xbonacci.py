class Test(object):
    def __init__(self,n):
        self.n = n

    @staticmethod
    def test_function(actual,expected):
        print("Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(actual) + " failed, expected " + str(expected))



def fibonacci(n):
    c, fib = 0, [0, 1]
    if n<1: return n
    else:
        while c < n:
            next = fib[c] + fib[c + 1]
            fib.append(next)
            c+=1
            if n <= next:break
    return fib


def xbonacci(signature,n):
    pass