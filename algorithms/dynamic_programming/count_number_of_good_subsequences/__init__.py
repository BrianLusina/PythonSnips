from collections import Counter


def count_good_subsequences_with_combinatorics(s: str) -> int:
    """
    Count the number of good subsequences of s.
    A good subsequence has equal frequency for all characters in it

    Args:
        s (str): input string
    Returns:
        int: number of good subsequences
    """
    n = len(s) + 1
    mod = 10**9 + 7

    # factorial[i] = i! mod MOD
    factorial = [1] * n
    # inverse_factorial[i] = (i!)^(-1) mod MOD
    inverse_factorial = [1] * n

    def quick_modular_inverse(base, exponent, modulus):
        """
        Method to find the modular inverse of a number
        """
        # Initialize the result to 1, as 1 is the identity element for multiplication modulo modulus
        result = 1

        while exponent != 0:
            # If exponent is odd, multiply result by base and take modulo modulus
            if (exponent & 1) == 1:
                result = result * base % modulus
            # Right shift exponent by 1 (equivalent to dividing exponent by 2)
            exponent >>= 1
            # Square base and take modulo modulus to reduce base in terms of modulus
            base = base * base % modulus

        return result

    def comb(number_of_items, number_of_items_to_choose):
        """
        Calculate binomial coefficient C(n, k) mod MOD. n choose k

        Args:
            number_of_items: Total number of items
            number_of_items_to_choose: Number of items to choose

        Returns:
            C(n, k) mod MOD
        """
        return (
            factorial[number_of_items]
            * inverse_factorial[number_of_items_to_choose]
            * inverse_factorial[number_of_items - number_of_items_to_choose]
            % mod
        )

    # Precompute factorials and their modular inverses.
    # Calculating the factorial and inverse of all numbers from 1 to n
    # instead of calculating factorial of a number again and again
    # we will store the factorial of a number i
    # and use to calculate the factorial of a number i+1, since
    # the factorial of a number i+1 is factorial of i-1 * i
    for i in range(1, n):
        factorial[i] = factorial[i - 1] * i % mod
        # Using Fermat's Little Theorem: a^(-1) ≡ a^(p-2) (mod p) where p is prime. Note that either pow built in can b
        # used or the quick_modular_inverse method can be used.
        # inverse_factorial[i] = pow(factorial[i], mod - 2, mod)
        inverse_factorial[i] = quick_modular_inverse(factorial[i], mod - 2, mod)

    # Count the frequency of each character in the string
    char_frequency = Counter(s)

    final_count = 0

    # Try each possible frequency (each character appears exactly i times)
    max_frequency = max(char_frequency.values())

    for target_freq in range(1, max_frequency + 1):
        # Count ways to form subsequences where each character appears exactly target_freq
        ways = 1

        for char_count in char_frequency.values():
            # For this character, we can either:
            # 1. Include it (choose target_freq occurrences from char_count)
            # 2. Exclude it (multiply by 1)
            # Total ways = C(char_count, target_freq) + 1)
            if char_count >= target_freq:
                ways = ways * (comb(char_count, target_freq) + 1) % mod

        final_count = (final_count + ways - 1) % mod

    return final_count
