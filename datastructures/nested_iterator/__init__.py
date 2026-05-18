from typing import List, Optional


class NestedInteger:
    # Constructor initializes a single integer if a value has been passed
    # else it initializes an empty list
    def __init__(self, integer=None):
        if integer:
            self.integer = integer
        else:
            self.n_list = []
            self.integer = 0

    # If this NestedIntegers holds a single integer rather
    # than a nested list, returns TRUE, else, returns FALSE
    def is_integer(self):
        if self.integer:
            return True
        return False

    # Returns the single integer, if this NestedIntegers holds a single integer
    # Returns null if this NestedIntegers holds a nested list
    def get_integer(self):
        return self.integer

    #  Sets this NestedIntegers to hold a single integer.
    def set_integer(self, value):
        self.n_list = None
        self.integer = value

    # Sets this NestedIntegers to hold a nested list and adds a nested
    # integer to it.
    def add(self, ni):
        if self.integer:
            self.n_list = []
            self.n_list.append(NestedInteger(self.integer))
            self.integer = None
        self.n_list.append(ni)

    # Returns the nested list, if this NestedIntegers holds a nested list
    # Returns null if this NestedIntegers holds a single integer
    def get_list(self):
        return self.n_list


class NestedIterator:
    def __init__(self, nested_list: List[NestedInteger]):
        """
        Initialize the iterator with a nested list
        Flatten the nested structure into a simple list of integers
        Args:
            nested_list (List[NestedInteger]): A list of NestedInteger objects that may contain integers or nested lists
        """

        def flatten_nested_list(nested: List[NestedInteger]) -> None:
            """
            Recursively flatten a nested list structure using depth first search. This is the core of the solution
            Args:
                nested: List[NestedInteger]: A list of nested integer objects to flatten
            """
            for nested_integer in nested:
                if nested_integer.is_integer():
                    # If it is a single integer, add it to the flattened list
                    self.flattened_list.append(nested_integer.get_integer())
                else:
                    flatten_nested_list(nested_integer.get_list())

        # Initialize the flattened list to store all integers
        self.flattened_list = []
        # Initialize the current index pointer (starts at -1, will be incremented before first access
        self.current_index = -1
        # Flatten the entire nested list structure
        flatten_nested_list(nested_list)

    def next(self) -> int:
        """
        Return the next integer in the iteration
        Returns:
            int: The next integer in the iteration
        """
        # Move to the next position
        self.current_index += 1
        # Return the integer at the current position
        return self.flattened_list[self.current_index]

    def has_next(self) -> bool:
        """
        Check if there are more integers to iterate over.
        Returns:
            bool: True if there are more integers to iterate over
        """
        # Check if the next position is within bounds
        return self.current_index + 1 < len(self.flattened_list)


class NestedIteratorV2:
    """
    This version uses a stack and iterator approach to flatten the list of NestedInteger objects
    """

    def __init__(self, nested_list: List[NestedInteger]):
        """
        Initialize the iterator with a nested list.
        Flatten the nested structure into a simple list of integers
        Args:
            nested_list (List[NestedInteger]): A list of NestedInteger objects that may contain integers or nested lists
        """
        self.nested_list_stack = list(reversed(nested_list))

    def next(self) -> Optional[int]:
        """
        Return the next integer in the iteration
        Returns:
            int: The next integer in the iteration
        """
        if self.has_next():
            return self.nested_list_stack.pop().get_integer()
        return None

    def has_next(self) -> bool:
        """
        Check if there are more integers to iterate over.
        Returns:
            bool: True if there are more integers to iterate over
        """
        # Iterate through the stack while the stack is not empty
        while len(self.nested_list_stack) > 0:
            # Save the top value of the stack
            top = self.nested_list_stack[-1]
            # If the top value is an integer, if true, return True. If not continue
            if top.is_integer():
                return True

            # if the top is not an integer, it must be the list of integers. Ppop the list from the stack and save it in
            # the top_list
            top_list = self.nested_list_stack.pop().get_list()
            # Save the length of the top_list in i and iterate in the list
            i = len(top_list) - 1
            while i >= 0:
                # Append the values of the nested list into the stack
                self.nested_list_stack.append(top_list[i])
                i -= 1
        return False
