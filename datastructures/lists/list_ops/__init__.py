from functools import reduce, wraps


class ListOps(object):
    @staticmethod
    def map_clone(function, xs):
        """
        Applies function on all elements in the xs
        :param function: Function to apply
        :param xs: list or tuple of elements to apply the function on
        :return: A new set of list elements with the function applied to each
        :rtype: list
        """
        for x in xs:
            yield function(x)

    @staticmethod
    def length(xs):
        """
        Will evaluate the length of the element xs and return its value
        :param xs: an iterable element
        :return: The length of the iterable element
        :rtype: int
        """
        count = 0
        for i in xs:
            if i:
                count += 1
        return count

    @staticmethod
    def filter_clone(function, xs):
        """
        Filters an iterable based on the predicate of the function
        :param function: The function that will be used to evaluate the iterable xs
        :param xs: iterable object
        :return: All the elements that meet the predicate of the function
        """
        for x in xs:
            if function(x):
                yield x

    @staticmethod
    def reverse(xs):
        """
        Reverses the order of the original iterable element, the first becomes last and vice versa
        :param xs: Iterable object
        :return: a reversed iterable object
        """
        return xs[::-1]

    @staticmethod
    def append(xs, y):
        """
        Adds element y onto the end of the iterable xs
        :param xs: Iterable object
        :param y: element to add to the end of the iterable
        :return: a new iterable object with y added to the end
        """
        xs.append(y)

        return xs

    @staticmethod
    def foldl(function, xs, acc):
        """
        Performs an operation on the sequence, reducing it to a single value
        :param function: Function to perform on iterable object
        :param xs: a sequence of objects, either strings or numbers
        :param acc: The accumulator
        :return: a reduced iterable object
        """
        return reduce(function, xs, acc)

    @staticmethod
    def flip(func):
        """
        Flips a function, creates a new function from the original with the arguments in reversed order
        :param func: the function to flip
        :return: a new function with the arguments flipped
        """

        @wraps(func)
        def new_func(*args):
            return func(*args[::-1])

        return new_func

    def foldr(self, function, xs, acc):
        """
        Folds the xs iterable from the right and reduces it to a single value
        :param function: function to perform operation
        :param xs: the iterable object to perform operation on
        :param acc: the accumulative element
        :return: a new object created from folding the iterable
        """
        return reduce(self.flip(function), self.reverse(xs), acc)

    def flat(self, xs):
        """
        Flattens a nested iterable xs to a single list or tuple
        :param xs: The xs
        :return: A flattened iterable
        :rtype: list or tuple
        """
        result = []
        for x in xs:
            if isinstance(x, (list, tuple)):
                for j in self.flat(x):
                    result.append(j)
            else:
                result.append(x)
        return result

    @staticmethod
    def concat(xs, ys):
        """
        Adds 2 iterables together and returns a new list with elements in both lists joined in final list
        :param xs: left list of elements
        :param ys: right list of elements
        :return: A list with elements from both lists
        :rtype: list
        """
        if xs is None:
            return ys
        if ys is None:
            return xs
        else:
            return xs + ys
