"""
Demonstration of using generators to find prime numbers. This will demonstrate using
custom classes with the __iter__ and __next__ functions and using generator expressions to 
achieve the same outcome
"""

# maximum number we want to reach
max_number = 50


def check_prime(number):
    """
    Checks if the given number is prime
    :param: number Number to evaluate for primality
    :rtype: bool True if the number is a prime, false otherwise
    """
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


class Primes(object):
    def __init__(self, max):
        """
        Creates a Primes Object with the max number as an attribute
        Will initialize number to 1
        :rtype: Primes
        """
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        """
        Will generate prime numbers lazily and raise a Stop Iteration when the currently evaluating
        number is equal to or greater than the maximum number
        :rtype: int
        :raises: StopIteration when the number is greater than or equal to maximum
        :return: next of the number if it is prime
        """
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()


def prime_generator(max_number):
    """
    Prime generator function that yields prime numbers less than the maximum number given
    This returns a generator object
    """
    number = 1
    while number < max_number:
        number += 1
        if check_prime(number):
            yield number


# we can do better and use a generator expression
prime_expression = (x for x in range(2, max_number) if check_prime(x))

if __name__ == "__main__":
    def custom_iterator(number):
        print("Using custom generator")
        primes = Primes(number)
        print(primes)
        for x in primes:
            print(x)


    custom_iterator(max_number)

    print("using generator function {}".format(prime_generator.__name__))
    prime_gen = prime_generator(max_number)
    print(prime_gen)
    for x in prime_gen:
        print(x)

    print("Using generator expression {}".format(prime_expression.__name__))
    print(prime_expression)
    for x in prime_expression:
        print(x)
