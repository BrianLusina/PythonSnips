from collections import defaultdict
import random


class RandomizedSet:

    def __init__(self):
        # _container to store the key value pairs where the key is the value in the set and the value is the index of
        # the value in the data list
        self._container_map = defaultdict(int)
        # _data that will also contain the items in the randomized set and will be used to retrieve random items
        self._data = []

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise
        Args:
            val (int): item to insert.
        Returns:
            bool:  Returns true if the item was not present, false otherwise
        """
        if val in self._container_map:
            return False

        # add the element to the dictionary. Setting the value as the
        # length of the list will accurately point to the index of the
        # new element. (len(some_list) is equal to the index of the last item +1)
        self._container_map[val] = len(self._data)
        self._data.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        Args:
            val (int): item to remove.
        Returns:
            bool:  Returns true if the item was present, false otherwise.
        """
        if val not in self._container_map:
            return False

        # essentially, we're going to move the last element in the list  into the location of the element we want to
        # remove. This is a significantly more efficient operation than the obvious solution of removing the item and
        # shifting the values of every item in the dictionary to match their new position in the list
        index = self._container_map[val]
        # since pop will always return the last element in the data list, we can use this instead of:
        # self._data[-1] and then later self._data.pop()
        last_element = self._data.pop()
        self._container_map[last_element] = index
        self._data[index] = last_element

        self._container_map.pop(val)
        return True

    def get_random(self) -> int:
        """
        Returns a random element from the current set of elements. Each element must have the same probability of being
        returned.

        Returns:
            int: random element from the set
        """
        if len(self._container_map) == 0:
            raise Exception("Set is empty")
        return random.choice(self._data)
