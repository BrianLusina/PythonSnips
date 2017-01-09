class Palindrome(object):
    """
    Palindrome class to handle Palindrome problems
    Notes regarding the implementation of smallest_palindrome and
    largest_palindrome:

    Both functions must take two keyword arguments:
        max_factor -- int
        min_factor -- int, default 0

    Their return value must be a tuple (value, factors) where value is the
    palindrome itself, and factors is an iterable containing both factors of the
    palindrome in arbitrary order.
    """

    def __init__(self):
        pass

    def is_palindrome(self, a):
        return str(a) == str(a)[::-1]

    def longest_palindrome(self, s):
        s, final_str = s.lower(), ""
        if s == "":
            return 0
        else:
            for y, item in enumerate(s):
                for x, item in enumerate(s):
                    tr = s[y:x + 1]
                    if self.is_palindrome(tr) and (len(tr) > len(final_str)):
                        final_str = tr

        return len(final_str)

    def palindrome_pairs(self, words):
        m = []
        for x in range(len(words) - 1, 0, -1):
            for i in range(x):
                if self.is_palindrome(str(words[i]) + str(words[i + 1])):
                    w1 = words[i]
                    w2 = words[i + 1]
                    m.append([words.index(w1), words.index(w2)])
        return m

    def smallest_palindrome(self, max_factor, min_factor=0):
        pass

    def largest_palindrome(self, max_factor, min_factor=0):
        pass
