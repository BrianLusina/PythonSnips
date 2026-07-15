from typing import List
import hashlib


class BloomFilter:
    """
    Space-efficient probabilistic data structure for data deduplication.
    Used to quickly check if we've seen a data item before.
    """

    def __init__(self, size: int = 10000, hash_count: int = 3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size

    def _hashes(self, item: str) -> List[int]:
        """Generate multiple hash values for an item"""
        hashes = []
        for i in range(self.hash_count):
            hash_val = int(hashlib.md5(f"{item}{i}".encode()).hexdigest(), 16)
            hashes.append(hash_val % self.size)
        return hashes

    def add(self, item: str):
        """Add an item to the bloom filter"""
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = True

    def contains(self, item: str) -> bool:
        """Check if item might be in the set (may have false positives)"""
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))
