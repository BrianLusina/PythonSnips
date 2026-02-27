from typing import Any


class Item:
    """
    Represents an item in the HashMap
    """

    def __init__(self, key: Any, data: Any):
        """
        Creates an instance of an Item in the HashMap.
        Args:
            key: The key of the item.
            data: The data of the item.
        """
        self.key = key
        self.data = data
