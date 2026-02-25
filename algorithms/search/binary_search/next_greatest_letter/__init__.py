from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    left = 0
    right = len(letters) - 1

    while left <= right:
        mid = (left + right) // 2

        if target >= letters[mid]:
            left = mid + 1
        else:
            right = mid - 1

    # When left > right, left denotes the index of the smallest character that is lexicographically greater than target.
    # This is because all characters at indices greater than right would be greater than target and character immediately
    # next to index right would be left (or right + 1) after the completion of binary search algorithm.
    # At the end of the binary search algorithm, left will store the index of the smallest character that is
    # lexicographically greater than target.

    # If left == letters.length, it means there is no character in letters that is lexicographically greater than target.
    # We return letters[0]. Otherwise, we return letters[left] as left holds the smallest character greater than target.

    if left == len(letters):
        return letters[0]
    else:
        return letters[left]
