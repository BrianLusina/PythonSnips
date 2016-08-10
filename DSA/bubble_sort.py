import unittest


class BubbleSort(object):
    """
    Uses various methods to perform a bubble sort in a list in Python
    :bubbly_ascend, sorts a list in ascending order without using inbuilt functions
    loops through the range of length of the list in reverse order and loops through each range of the number obtained
    performs a check to see if the current item is greater than the next item, if so, stores it in a temp variable
    reassigns the smaller value to the index of the larger item and reassigns the temp variable to the small variable
    :returns the sorted list
    :bubbly_descend, does the opposite of bubbly_ascend
    """
    def __init__(self, list_sort):
        self.list_sort = list_sort

    def bubbly_ascend(self):
        for p_num in range(len(self.list_sort)-1, 0, -1):
            for x in range(p_num):
                if self.list_sort[x] > self.list_sort[x + 1]:
                    temp = self.list_sort[x]
                    self.list_sort[x] = self.list_sort[x + 1]
                    self.list_sort[x+1] = temp
        return self.list_sort

    def bubbly_descend(self):
        for p_num in range(len(self.list_sort) - 1, 0, -1):
            for x in range(p_num):
                if self.list_sort[x] < self.list_sort[x + 1]:
                    temp = self.list_sort[x]
                    self.list_sort[x] = self.list_sort[x + 1]
                    self.list_sort[x + 1] = temp
        return self.list_sort


class Tests(unittest.TestCase):
    def test_1(self):
        bubbles = BubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        self.assertEqual(bubbles.bubbly_ascend(), sorted([54, 26, 93, 17, 77, 31, 44, 55, 20]))

    def test_2(self):
        bubbles = BubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        self.assertEqual(bubbles.bubbly_descend(), sorted([54, 26, 93, 17, 77, 31, 44, 55, 20], reverse=True))
