def reverse_string(phrase: str) -> str:
    """
    Reverses a string. Takes O(n) time complexity as we have to traverse each word in the string. And O(n) space
    complexity as we use a list to store the words we reverse.
    @param phrase: string to reverse
    @return: reversed string
    @rtype: str
    """
    words = phrase.split(" ")

    result = [word for word in words[::-1] if word.isalnum()]

    return " ".join(result)
