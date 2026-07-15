from typing import List, Set
from itertools import permutations


def num_tile_possibilities(tiles: str) -> int:
    # Store unique sequences to avoid duplicates
    unique_letter_sets: Set[str] = set()

    # Sort characters to handle duplicates efficiently
    sorted_tiles: str = "".join(sorted(tiles))

    def generate_sequences(current: str, index: int):
        # Recursively generates all possible sequences by including/excluding each tile.
        # Once a new sequence is found, its unique permutations are counted.
        if index >= len(sorted_tiles):
            # If a new sequence is found, count its unique permutations
            if current not in unique_letter_sets:
                unique_letter_sets.add(current)

                total_permutations = len(set(permutations(current)))
                return total_permutations
            return 0

        # Explore two possibilities: skipping the current character or including it
        without_letter = generate_sequences(current, index=index + 1)
        with_letter = generate_sequences(current + sorted_tiles[index], index=index + 1)

        # Return all the possible sequences
        return without_letter + with_letter

    # Optionally, you can write the count_permutations and the factorial method if not using builtin methods
    # def factorial(n):
    #
    #     # Computes the factorial of a given number.
    #     if n <= 1:
    #         return 1
    #
    #     result = 1
    #     for num in range(2, n + 1):
    #         result *= num
    #     return result
    #
    # def count_permutations(sequence):
    #
    #     # Calculates the number of unique permutations of a sequence, accounting for duplicate characters.
    #     permutations = factorial(len(sequence))
    #
    #     # Adjust for repeated characters by dividing by factorial of their counts
    #     for count in Counter(sequence).values():
    #         permutations //= factorial(count)
    #
    #     return permutations

    output = generate_sequences("", 0)

    return output - 1


def num_tile_possibilities_with_recursion(tiles: str) -> int:
    sequences: Set[str] = set()
    used: List[bool] = [False] * len(tiles)

    def generate_sequences(current: str) -> None:
        sequences.add(current)

        for idx, char in enumerate(tiles):
            if not used[idx]:
                used[idx] = True
                generate_sequences(current + char)
                used[idx] = False

    generate_sequences("")
    return len(sequences) - 1


def num_tile_possibilities_with_optimized_recursion(tiles: str) -> int:
    char_count: List[int] = [0] * 26
    for letter in tiles:
        char_count[ord(letter) - ord("A")] += 1

    def generate_sequences() -> int:
        result = 0
        for idx in range(26):
            if char_count[idx] == 0:
                continue

            result += 1
            char_count[idx] -= 1
            result += generate_sequences()
            char_count[idx] += 1

        return result

    return generate_sequences()
