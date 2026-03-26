from collections import defaultdict


def appeal_sum_dp(s: str) -> int:
    # Total sum of appeals across all substrings
    total_appeal_sum = 0
    # Current contribution to appeal from substrings ending at current position
    current_contribution = 0
    # Track the last seen position of each character (a-z)
    # Initialize with -1 to indicate character hasn't been seen yet
    last_position = [-1] * 26

    for idx, char in enumerate(s):
        # Convert character to index (0-25 for a-z)
        char_index = ord(char) - ord('a')
        # Calculate new substrings that include current character
        # These are all substrings from (last occurrence of char + 1) to current_index
        # Each adds 1 to the appeal count if char wasn't in that substring before
        current_contribution += idx - last_position[char_index]
        # Add current contribution to total
        # This represents appeal sum of all substrings ending at current_index
        total_appeal_sum += current_contribution

        # Update last seen position of current character
        last_position[char_index] = idx

    return total_appeal_sum

def appeal_sum_hash_table(s: str) -> int:
    # Create a hash map to track the last occurrence index of each character
    track = defaultdict(lambda: -1)

    # Initialize result variable to accumulate the total appeal sum
    appeal = 0

    # Get the length of the string
    n = len(s)

    # Iterate through each character in the string with its index
    for i, c in enumerate(s):
        # Calculate the contribution of the current character to the appeal sum
        # (i - track[c]) gives the number of substrings ending with c
        # (n - i) gives the number of substrings starting from index i to the end of the string
        appeal += (i - track[c]) * (n - i)

        # Update the last occurrence index of the c to the current index
        track[c] = i

    # Return the total appeal sum
    return appeal