def spreadsheet_encode_column(column_id: str) -> int:
    """
    Encodes a Spreadsheet column ID as an integer and returns it. Here the encoding uses the alphabets A, B, C, etc. and
    further uses the indexing of the alphabet starting from 1 like: A=1, B=2, C=3,..., Z=26

    Complexity
    Where n represents the number of characters in the column_id

    - Time O(n) as we iterate over each character in the column ID to calculate the encoding
    - Space O(1) no extra space is required to perform the encoding

    Args:
        column_id (str): the column ID(name) as represented on a spreadsheet
    Returns:
        int: encoded column id as an integer
    """
    num = 0
    # count will help in determining the power of the base as we convert the column id into the corresponding integer
    count = len(column_id) - 1

    for char in column_id:
        # we use the base 26 system here as there are 26 letters in the alphabet
        # ord(char) returns the unicode code point for char. In order to make sure that A=1, we need to determine the
        # relative difference from the result given by ord & from the representation we require for base 26 system
        # Now we know that ord('A') equals 65. So if we find the Unicode code point using ord() of a character,
        # subtract ord('A') from it, and then add 1 to it, we’ll get the representation we want for the base 26 system
        num += 26**count * (ord(char) - ord("A") + 1)

        # count is decremented by 1 as the power of the base decrements by 1 from the digits from left to right
        count -= 1

    return num
