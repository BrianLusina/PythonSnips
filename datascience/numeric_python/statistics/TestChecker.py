"Class to test truths of functions"


class Test(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def test_function(actual, expected):
        print
        "Test for " + str(actual) + " passed " if actual == expected else "Test for " + str(
            actual) + " failed, expected " + str(expected)
