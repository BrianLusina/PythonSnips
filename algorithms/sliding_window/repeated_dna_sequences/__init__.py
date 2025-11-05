from typing import List, Dict


def find_repeated_dna_sequences_naive(dna_sequence: str) -> List[str]:
    """
    Finds all repeated DNA sequences in a given string.

    A repeated DNA sequence is a subsequence that appears more than once in the given string.
    The function returns a list of all repeated DNA sequences found in the given string.
    Parameters:
        dna_sequence (str): The string to search for repeated DNA sequences.

    Returns:
        List[str]
    """
    result_set = set()
    seen: Dict[str, bool] = {}
    for idx in range(len(dna_sequence)):
        subsequence = dna_sequence[idx:idx+10]
        if subsequence in seen:
            result_set.add(subsequence)
        else:
            seen[subsequence]=True

    return list(result_set)

def find_repeated_dna_sequences(dna_sequence: str) -> List[str]:
    """
    Finds all repeated DNA sequences in a given string.

    A repeated DNA sequence is a subsequence that appears more than once in the given string.
    The function returns a list of all repeated DNA sequences found in the given string.
    Parameters:
        dna_sequence (str): The string to search for repeated DNA sequences.

    Returns:
        List[str]
    """
    to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    encoded_sequence = [to_int[c] for c in dna_sequence]

    dna_sequence_substr_length, dna_sequence_length = 10, len(dna_sequence) # Length of DNA sequence to check

    if dna_sequence_length <= dna_sequence_substr_length:
        return []

    base_a_encoding = 4 # Base-4 encoding
    rolling_hash_value = 0
    seen_hashes, output = set(), set()
    a_k = 1  # Stores a^k for hash updates

    # # Compute the initial hash using base-4 multiplication
    for i in range(dna_sequence_substr_length):
        rolling_hash_value = rolling_hash_value * base_a_encoding + encoded_sequence[i]
        a_k *= base_a_encoding # Precompute a^k for later use in rolling hash updates

    seen_hashes.add(rolling_hash_value) # Store the initial hash

    # Sliding window approach to update the hash efficiently
    for start in range(1, dna_sequence_length - dna_sequence_substr_length + 1):
        # Remove the leftmost character and add the new rightmost character
        rolling_hash_value = rolling_hash_value * base_a_encoding - encoded_sequence[start - 1] * a_k + encoded_sequence[start + dna_sequence_substr_length - 1]

        # If this hash has been seen_hashes before, add the corresponding substring to the output
        if rolling_hash_value in seen_hashes:
            output.add(dna_sequence[start: start + dna_sequence_substr_length])
        else:
            seen_hashes.add(rolling_hash_value)

    # Convert set to list before returning
    return list(output)

