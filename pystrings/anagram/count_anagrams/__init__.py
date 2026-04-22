from typing import Counter
from collections import Counter


def count_anagrams(s: str) -> int:
    # Define modulo constant for large number calculations
    mod = 10**9 + 7
    # Define maximum possible word length
    max_len = 10**5

    # Arrays to store precomputed factorials and their modular inverses
    factorials = [1] * (max_len + 1)
    inv_factorials = [1] * (max_len + 1)

    def pre_compute():
        """
        Precomputes factorials and their modular inverses using Fermat's theorem.
        This allows efficient computation of permutations involving repeated characters
        """
        # Compute factorials modulo MOD
        factorials[0] = 1
        for i in range(2, max_len + 1):
            factorials[i] = factorials[i - 1] * i % mod

        # Compute modular inverse of MAX_LEN! using Fermat's Little Theorem
        inv_factorials[max_len] = pow(factorials[max_len], mod - 2, mod)

        # Compute modular inverses for all numbers from MAX_LEN-1 down to 1
        for i in range(max_len - 1, 0, -1):
            inv_factorials[i] = inv_factorials[i + 1] * (i + 1) % mod

    def count_permutations(w: str) -> int:
        """
        Computes the number of distinct permutations of a given word, considering repeated characters
        """
        # Count occurrences of each character
        letter_count: Counter = Counter(w)

        # Compute n! for total characters
        total_permutations = factorials[len(w)]

        # Divide by factorial of each character count to account for duplicates
        for freq in letter_count.values():
            total_permutations = (total_permutations * inv_factorials[freq]) % mod

        return total_permutations

    result = 1
    pre_compute()
    words = s.split()

    # Multiply the permutations of each word to get the final count
    for word in words:
        result = (result * count_permutations(word)) % mod

    return result
