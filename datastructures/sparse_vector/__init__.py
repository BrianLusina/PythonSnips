from typing import List, Dict


class SparseVector:
    def __init__(self, nums: List[int]):
        # Dictionary comprehension here initializes the elements hashmap/dictionary with index value key value pairs and
        # filters out the 0 values. 0 in Python evaluates to False.
        self.non_zero_elements: Dict[int, int] = {
            idx: value for idx, value in enumerate(nums) if value != 0
        }

    def dot_product(self, vec: "SparseVector") -> int:
        # extract the hash maps of the sparse vectors, current_vector_data and the other_vector_elements.
        current_vector_data, other_vector_data = (
            self.non_zero_elements,
            vec.non_zero_elements,
        )

        # Now we choose the smaller of the two to iterate over and swap
        if len(other_vector_data) < len(current_vector_data):
            current_vector_data, other_vector_data = (
                other_vector_data,
                current_vector_data,
            )

        # compute the dot product
        return sum(
            value * other_vector_data.get(idx, 0)
            for idx, value in current_vector_data.items()
        )
