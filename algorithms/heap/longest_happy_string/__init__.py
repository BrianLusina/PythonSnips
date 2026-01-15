from typing import List, Tuple
from heapq import heappop, heappush


def longest_diverse_string(a: int, b: int, c: int) -> str:
    # Priority queue (max heap) to store the counts of 'a', 'b', and 'c' as negative values
    max_heap: List[Tuple[int, str]] = []

    # Push the counts of each character into the heap if they are greater than 0
    if a > 0:
        heappush(max_heap, (-a, "a"))  # Push 'a' with its count
    if b > 0:
        heappush(max_heap, (-b, "b"))  # Push 'b' with its count
    if c > 0:
        heappush(max_heap, (-c, "c"))  # Push 'c' with its count

    # List to store the characters of the resulting happy string
    result = []

    # Process the heap until it's empty or no valid character can be added
    while max_heap:
        # Pop the character with the highest remaining frequency
        count, character = heappop(max_heap)
        count = -count  # Convert back to positive

        # Check if adding this character violates the "no three consecutive" rule
        if len(result) >= 2 and result[-1] == character and result[-2] == character:
            # If the rule is violated and no alternative character exists, break the loop
            if not max_heap:
                break

            # Use the next most frequent character temporarily
            temp_cnt, temp_char = heappop(max_heap)
            result.append(temp_char)  # Add the alternative character to the result

            # Push the alternative character back with its updated count
            if (temp_cnt + 1) < 0:
                heappush(max_heap, (temp_cnt + 1, temp_char))

            # Push the original character back to the heap to try adding it later
            heappush(max_heap, (-count, character))
        else:
            # If no violation, add the current character to the result
            count -= 1  # Decrease its count
            result.append(character)

            # Push the character back into the heap if it still has remaining occurrences
            if count > 0:
                heappush(max_heap, (-count, character))

    # Join the list into a string and return as the final result
    return "".join(result)
