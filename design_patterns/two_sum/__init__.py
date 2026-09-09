from collections import defaultdict


class TwoSum:
    """
    A data structure that supports adding numbers and finding if two numbers sum to a target value.
    """

    def __init__(self):
        """
        Initialize the data structure with a hash map to store number frequencies.
        """
        # Dictionary to store each number and its count
        self.counter = defaultdict(int)

    def add(self, number: int):
        """
        Add a number to the data structure.

        Args:
            number: The integer to add to the collection
        """
        # Increment the count for this number
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        """
        Check if there exist two numbers in the collection that sum to the given value.

        Args:
            value: The target sum to find

        Returns:
            True if two numbers exist that sum to value, False otherwise
        """
        # Iterate through each unique number in our collection
        for number, count in self.counter.items():
            # Calculate the complement needed to reach the target value
            complement = value - number
            if complement in self.counter:
                # If num and complement are different, we found a valid pair
                # If they're the same, we need at least 2 occurrences of that number
                if number != complement or count > 1:
                    return True

        return False
