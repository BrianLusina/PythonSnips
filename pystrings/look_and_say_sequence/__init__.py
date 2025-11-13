from typing import List


def look_and_say_sequence(sequence: str) -> str:
    """
    Counts the number of occurrences of each character in the provided sequence and returns the count of each character
    alongside the character itself as a string in the format `cx`, where c is the count and x is the character. This
    retains the sequence order passed in and only includes the counts

    Args:
        sequence (str): sequence of characters, e.g. "11" or "121", etc

    Returns:
        str: string in the format of count of characters along with the characters themselves,
        e.g. if sequence is "1", return will be "11"

    Complexity:
    Time: O(n) where n is the number of characters in the provided sequence as the algorithm has to iterate over each
    character in the sequence
    Space: O(n) where n is the number of characters in the provided sequence. This is because the algorithm uses a list
    to store the count of characters and the characters themselves to later join into a string as the result
    """
    result: List[str] = []
    i = 0

    while i < len(sequence):
        # count is reset to one to keep track of the current count of the sequence
        count = 1

        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            # here we keep track of consecutive similar characters and increase their count if we encounter them.

            i += 1
            count += 1

        # the string version of the count of the character is added along with the character itself to the resulting
        # list
        result.append(str(count) + sequence[i])
        # we increment the i variable to move to the next character in the sequence
        i += 1

    return "".join(result)
