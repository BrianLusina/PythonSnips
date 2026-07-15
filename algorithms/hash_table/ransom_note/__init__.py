from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Checks if it is possible to construct a ransom note from the given letters in the magazine where each letter in the
    magazine can only be used once. If a letter in the magazine occurs more than once, it can only be used that many
    number of times, so `magazine=aabc`, means we can use letter a twice, but not more than that.

    Complexity Analysis:

    Time O(n + m): Where n is the number of letters in `ransom_note` and `m` is the number of letters in `magazine`. This
    is because we iterate through the magazine to count occurrences of the number of letters and again through ransom_note
    to check if each letter is present in the magazine

    Space O(1): Since there are only English letters which are 26, the space used by the hash table is always count going
    to be constant.

    Args:
        ransom_note(str): the string with which we intend to construct from the magazine.
        magazine(str): the string with which we intend to use to construct ransom_note
    Returns:
        bool: True if we can construct ransom note from the magazine, false otherwise.
    """
    # No need to proceed if we don't have a magazine to construct a ransom note from
    if not magazine:
        return False

    # Count the number of occurrences of each letter in the magazine. This will be used to keep track of the number of
    # letters we can use when constructing the ransom note
    occurrences = Counter(magazine)

    # Iterate through each letter in the ransom note to check if it is in the magazine
    for letter in ransom_note:
        # If a letter does not exist in the frequency map of the magazine or the count has now become 0 meaning we can't
        # use the letter from the magazine, then there is no need to proceed with the iteration, we can't construct
        # the ransom note
        if letter not in occurrences or occurrences[letter] == 0:
            return False

        # if the letter is in the occurrences, we decrease the count of the occurrences of the letter and the number
        # of letters left to construct the ransom note
        occurrences[letter] -= 1

    return True


def can_construct_2(ransom_note: str, magazine: str) -> bool:
    # create an empty hash map to store the frequency of each character in the magazine string
    frequency = {}

    for char in magazine:
        # if character is already present in hash map then increment
        # its frequency by 1
        if char in frequency:
            frequency[char] += 1

        # else count its first occurrence
        else:
            frequency[char] = 1

    for char in ransom_note:
        # if the character is not in the hash map or its count is 0, return False
        if char not in frequency or frequency[char] == 0:
            return False

        # otherwise, decrease the character's frequency in the hash map by 1
        else:
            frequency[char] -= 1

    return True
