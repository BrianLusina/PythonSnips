from typing import List


def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
    def lower_bound(items: List[str], start_index: int, word: str) -> int:
        """Binary search over the item list for the word starting at start index. Returns the index of the match. This
        assumes the item list is already sorted.
        Args:
            items (List): item list to search through
            start_index (int): start index
            word (str): word to search for in item list
        Returns:
            int: index of the match
        """
        left = start_index
        right = len(items)

        while left < right:
            mid = (left + right) // 2
            if items[mid] == word:
                right = mid
            else:
                left = mid + 1
        return left

    # contains the list to return
    result: List[List[str]] = []

    # we assume that it is allowed to sort the products in-place, modifying the input list
    # incurs an O(nlog(n)) time complexity
    products.sort()

    start = 0
    bs_start = 0
    number_of_products = len(products)

    # iterate each character in the search word, adding it to the prefix to search for
    prefix = ""
    for letter in search_word:
        prefix += letter

        # binary search for the prefix in the input to get the starting index
        start = lower_bound(products, bs_start, prefix)

        # add an empty list
        result.append([])

        # add the next 3 strings from the current binary search start index till the prefix remains the same
        # add the words with the same prefix to the result. Loop runs until i reaches the end of the input or 3 times
        # or till the prefix is the same for products[i] whichever comes first
        for i in range(start, min(start + 3, number_of_products)):
            if len(products[i]) < len(prefix) or products[i][0:len(prefix)] != prefix:
                break
            result[len(result) - 1].append(products[i])

        # reduce the size of elements to binary search on
        bs_start = abs(start)

    return result
