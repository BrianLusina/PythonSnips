from datastructures.trees.trie.trie_node import TrieNode


def is_prefix_of_word(sentence: str, search_word: str) -> int:
    """
    This function will check if a given search_word is a prefix of any word in a sentence.

    Parameters:
        sentence (str): The sentence to search in.
        search_word (str): The prefix to search for.

    Returns:
        int: The index of the word if the prefix is found, -1 otherwise.
    """
    trie = TrieNode()
    word_list = sentence.split(" ")

    # Insert the words into the trie with their respective index
    for index, word in enumerate(word_list, start=1):
        trie.insert(word, index)

    # Search for the prefix in the trie
    return trie.search_prefix(search_word)
