class BubbleSort(object):
    """
    Uses various methods to perform a bubble sort in a list in Python
    :bubbly_descend, does the opposite of bubbly_ascend
    """

    def __init__(self, list_sort):
        """
        Creates an object of BubbleSort
        :param list_sort: The item to use for the object creation. This param must be a list of integers
        :raises: ValueError
        """
        # check if item is a list
        if list_sort is None or not isinstance(list_sort, list):
            raise ValueError("Please input a list of integers/floats")

        # check if all items in the list are not integers
        elif not all(isinstance(item, (float, int)) for item in list_sort):
            raise ValueError("All elements of the list MUST be integers/floats")
        else:
            self.list_sort = list_sort

    def bubbly_ascend(self):
        """
        Sorts the list using bubble sort in ascending order without using inbuilt functions
        loops through the range of length of the list in reverse order and loops through each range of the number
         obtained
         performs a check to see if the current item is greater than the next item, if so, stores it in a temp
          variable
        reassigns the smaller value to the index of the larger item and reassigns the temp variable to the
        small variable
        :return: sorted list
        :rtype: list
        """
        # store the length of the list, this will reduce the number of calls to get the length of the list
        sorted_len = len(self.list_sort)

        # start counting down from length of the list to 1
        for p_num in range(sorted_len - 1, 0, -1):

            # doing this multiple times will move the smaller items to the left and the greater items to the right
            # count up from 0 to the first occurrence in the range, e.g. x in the 1st occurrence could be 5
            for x in range(p_num):

                # compare the 2 elements that share a border
                if self.list_sort[x] > self.list_sort[x + 1]:
                    # store the current item in a temp variable
                    temp = self.list_sort[x]

                    # store the smaller item in the position of the greater item
                    self.list_sort[x] = self.list_sort[x + 1]

                    # move the greater item to the position of the smaller item
                    self.list_sort[x + 1] = temp

        # return the sorted list
        return self.list_sort

    def bubbly_descend(self):
        for p_num in range(len(self.list_sort) - 1, 0, -1):
            for x in range(p_num):
                if self.list_sort[x] < self.list_sort[x + 1]:
                    temp = self.list_sort[x]
                    self.list_sort[x] = self.list_sort[x + 1]
                    self.list_sort[x + 1] = temp
        return self.list_sort
