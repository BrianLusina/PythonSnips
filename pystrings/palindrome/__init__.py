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

    @staticmethod
    def is_palindrome(a):
        return str(a) == str(a)[::-1]

    @staticmethod
    def longest_palindrome(s):
        s, final_str = s.lower(), ""
        if s == "":
            return 0
        else:
            for y, item in enumerate(s):
                for x, _ in enumerate(s):
                    tr = s[y: x + 1]
                    if Palindrome.is_palindrome(tr) and (len(tr) > len(final_str)):
                        final_str = tr

        return len(final_str)

    def palindrome_pairs(self, word_list):
        """
        Loops through the word_list and checks if the current word is a palindrome of any of the preceding words
        or if the preceding words are a palindrome of the current
        :param word_list: list of words to evaluate for palindrome pairs
        :return: list of lists with each list containing the word indices which form a palindrome
        """
        words = [str(word) for word in word_list]

        return [
            [i, j]
            for i, word_i in enumerate(words)
            for j, word_j in enumerate(words)
            if i != j and self.is_palindrome(word_i + word_j)
        ]

    def smallest_palindrome(self, max_factor, min_factor=0):
        """
        Gets the smallest palindrome from the generator and returns the value from the operation
        :param max_factor:Largest factor to evaluate
        :param min_factor: Smallest factor to evaluate
        :return: Smallest palindrome pair product,
        :rtype:int
        """
        return min(self.generate_palindromes(max_factor, min_factor), key=lambda tup: tup[0])

    def largest_palindrome(self, max_factor, min_factor=0):
        """
        Gets the maximum palindromr product from the generator function
        using the key to only fetch the value from the operation
        :param max_factor: The maximum factor or number to use
        :param min_factor: the minimum number to use, which defaults to 0 if there is no input
        :return: Maximum palindrome product from the generator
        :rtype:int
        """
        return max(self.generate_palindromes(max_factor, min_factor), key=lambda tup: tup[0])

    def generate_palindromes(self, max_factor, min_factor):
        """
        Creates 2 ranges one for the minimum factor and another for the maximum factor
        The results for the first one are used to generate a range for the second one
        Then checks if the product from the result of the 2 operations is a palindrome
        Returns only if the product results to a palindrome
        :return: Tuple with the first element as the product(value) and the 2nd element as the palindrome pair that
        make the product(factors)
        :rtype: tuple
        """
        return ((a * b, (a, b))
                for a in range(min_factor, max_factor + 1)
                for b in range(min_factor, a + 1)
                if self.is_palindrome(a * b)
                )
