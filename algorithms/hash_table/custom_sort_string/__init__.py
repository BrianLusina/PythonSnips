from collections import Counter


def custom_sort_string_custom_comparator(order: str, s: str) -> str:
    result = list(s)

    result.sort(key=lambda c: order.index(c) if c in order else len(order))

    return "".join(result)


def custom_sort_string_frequency_table(order: str, s: str) -> str:
    # Create a hash map to store the count of each character in s
    s_elem_freq = Counter(s)
    # Define result to build the final string
    s_permutation = []

    # Iterate through the order string
    for char in order:
        # Elem to be Ordered
        # Append char to result as many times as its recorded frequency
        if char in s_elem_freq:
            s_permutation.append(char * s_elem_freq[char])
            # Remove char from the hash map
            del s_elem_freq[char]

    # Append remaining characters to result
    for unordered_elem in s_elem_freq:
        s_permutation.append(unordered_elem * s_elem_freq[unordered_elem])

    # Return the result string
    return "".join(s_permutation)
