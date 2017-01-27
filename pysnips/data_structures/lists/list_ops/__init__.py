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
        Adds element y onto the end of the iterable
        :param xs: Iterable object
        :param y: element to add to the end of the iterable
        :return: a new iterable object with y added to the end
        """
        
        return xs

    @staticmethod
    def foldl(function, xs, acc):
        return xs

    @staticmethod
    def foldr(function, xs, acc):
        return xs

    @staticmethod
    def flat(xs):
        return xs

    @staticmethod
    def concat(xs, ys):
        return xs
