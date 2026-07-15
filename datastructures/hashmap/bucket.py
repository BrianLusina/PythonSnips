from typing import List, Any
from datastructures.hashmap.item import Item


class Bucket(object):
    def __init__(self):
        # Initialize an empty list to store key-value pairs
        self.bucket: List[Item] = []

    def get(self, key: Any) -> Any:
        # iterate through each key value pair in the bucket
        for item in self.bucket:
            # If the key matches the provided key, return the corresponding value
            if item.key == key:
                return item.data
        # if the key is not found, raise a key error and let the call site handle the error
        raise KeyError(f"Key {key} does not exist")

    def update(self, key: Any, value: Any) -> None:
        # Flag to indicate whether the key is found in the bucket
        found = False
        # Iterate through each key value pair in the bucket
        for idx, item in enumerate(self.bucket):
            current_key, current_value = item.key, item.data
            # If the key matches the key of the current key-valur pair
            if current_key == key:
                # Update the value of the key-value pair
                self.bucket[idx] = Item(key, value)
                # Set the blag to true, indicating the key is found and break out of the loop
                found = True
                break

        # if the key is not found in the bucket, add it along with its value
        if not found:
            self.bucket.append(Item(key, value))

    def remove(self, key: Any) -> None:
        # Iterate through each key-value pair in the bucket
        for idx, item in enumerate(self.bucket):
            current_key, current_value = item.key, item.data
            # If the key matches the key of the current key-value pair
            if current_key == key:
                # Delete the key-value pair from the bucket
                del self.bucket[idx]
                # Exit the loop as the key has been removed
                break
