from typing import List, Dict, Set
from datastructures.trees.trie import AlphabetTrie


def word_break_trie(s: str, word_dict: List[str]) -> List[str]:
    """
    This adds spaces to s to break it up into a sequence of valid words from word_dict.

    This uses a Trie to store the words in the dictionary and a map to store the results of subproblems.

    Complexity:
    Time: O(n*2^n): where n is the length of the string
    Space: O(n*2^n): where n is the length of the string

    Args:
        s: The input string
        word_dict: The dictionary of words
    Returns:
        List of valid sentences
    """
    # build the Trie from the word dictionary
    trie = AlphabetTrie()
    for word in word_dict:
        trie.insert(word)

    # map to store results of subproblems
    results: Dict[int, List[str]] = dict()

    # iterate from the end to the start of the string
    for start_idx in range(len(s), -1, -1):
        # store valid sentences starting from start_idx
        valid_sentences = []

        # initialize current node to the root of the Trie
        current_node = trie.root

        # iterate from start_idx to the end of the string
        for end_idx in range(start_idx, len(s)):
            char = s[end_idx]
            index = ord(char.lower()) - ord("a")

            # check if the current character exists in the trie
            if not current_node.children[index]:
                break

            # move to the next node in the trie
            current_node = current_node.children[index]

            # check if we have found a valid word
            if current_node.is_end_of_word:
                current_word = s[start_idx : end_idx + 1]

                # if it is the last word, add it as a valid sentence
                if end_idx == len(s) - 1:
                    valid_sentences.append(current_word)
                else:
                    # if it's not the last word, append it to each sentence formed by the remaining substring
                    sentences_from_next_index = results.get(end_idx + 1, [])
                    for sentence in sentences_from_next_index:
                        valid_sentences.append(f"{current_word} {sentence}")

        # store the valid sentences for the current start index
        results[start_idx] = valid_sentences

    # return the sentences formed from the entire string
    return results.get(0, [])


def word_break_dp_tabulation(s: str, word_dict: List[str]) -> List[str]:
    """
    This adds spaces to s to break it up into a sequence of valid words from word_dict.

    This uses dynamic programming with tabulation to store the words in the dictionary and a map to store the results
    of subproblems.

    Complexity:
    Time: O(n*2^n): where n is the length of the string
    Space: O(n*2^n): where n is the length of the string

    Args:
        s: The input string
        word_dict: The dictionary of words
    Returns:
        List of valid sentences
    """
    # Initializing the dp table of size s.length + 1
    dp = [[] for _ in range(len(s) + 1)]
    # Setting the base case
    dp[0] = [""]

    # For each substring in the input string, repeat the process.
    for i in range(1, len(s) + 1):
        prefix = s[:i]

        # An array to store the valid sentences formed from the current prefix being checked.
        temp = []

        # Iterate over the current prefix and break it down into all possible suffixes.
        for j in range(0, i):
            suffix = prefix[j:]

            # Check if the current suffix exists in word_dict. If it does, we know that it is a valid word
            # and can be used as part of the solution.
            if suffix in word_dict:
                # Retrieve the valid sentences from the previously computed subproblem
                for substring in dp[j]:
                    # Merge the suffix with the already calculated results
                    temp.append((substring + " " + suffix).strip())
        dp[i] = temp

    # returning all the sentences formed from the complete string s
    return dp[len(s)]


def word_break_dp_tabulation_2(s: str, word_dict: List[str]) -> List[str]:
    """
    This adds spaces to s to break it up into a sequence of valid words from word_dict.

    This uses dynamic programming with tabulation to store the words in the dictionary and a map to store the results
    of subproblems.

    Complexity:
    Time: O(n*2^n): where n is the length of the string
    Space: O(n*2^n): where n is the length of the string

    Args:
        s: The input string
        word_dict: The dictionary of words
    Returns:
        List of valid sentences
    """
    # map to store results of the subproblems
    dp: Dict[int, List[str]] = dict()

    # iterate from the end of the string to the beginning
    for start_idx in range(len(s), -1, -1):
        # store valid sentences starting from start_idx
        valid_sentences = []

        # Iterate from start index to the end of the string
        for end_idx in range(start_idx, len(s)):
            # extract substring from start_idx to end_idx
            current_word = s[start_idx : end_idx + 1]

            # Check if the current substring is a valid word
            if current_word in word_dict:
                # If it's the last word, add it as a valid sentence
                if end_idx == len(s) - 1:
                    valid_sentences.append(current_word)
                else:
                    # If it's not the last word, append it to each sentence formed by the remaining substring
                    sentences_from_next_index = dp.get(end_idx + 1, [])
                    for sentence in sentences_from_next_index:
                        valid_sentences.append(f"{current_word} {sentence}")

        # Store the valid sentences in dp
        dp[start_idx] = valid_sentences

    # returning all the sentences formed from the complete string s
    return dp.get(0, [])


def word_break_dp_memoization(s: str, word_dict: List[str]) -> List[str]:
    """
    This adds spaces to s to break it up into a sequence of valid words from word_dict.

    This uses dynamic programming with memoization to store the words in the dictionary and a map to store the results
    of subproblems.

    Complexity:
    Time: O(n*2^n): where n is the length of the string
    Space: O(n*2^n): where n is the length of the string

    Args:
        s: The input string
        word_dict: The dictionary of words
    Returns:
        List of valid sentences
    """
    word_set: Set[str] = set(word_dict)
    memoization: Dict[str, List[str]] = dict()

    def dfs(remaining_str: str, words_set: Set[str], memo: Dict) -> List[str]:
        """
        Depth-first search to find all possible word combinations
        Args:
            remaining_str(str): the remaining string to search through
            words_set(set): set of dictionary words to use to construct sentences
            memo(dict): dictionary to improve computation of already processed words
        Returns:
            list: possible word combinations
        """
        # check if the result for this substring is already memoized
        if remaining_str in memo:
            return memo[remaining_str]

        # base case: when the string is empty, return a list containing an empty string
        if not remaining_str:
            return [""]

        results = []
        for i in range(1, len(remaining_str) + 1):
            current_word = remaining_str[:i]
            # if the current substring is a valid word in the word set
            if current_word in words_set:
                for next_word in dfs(remaining_str[i:], words_set, memo):
                    # append current word and next word
                    results.append(
                        f"{current_word}{" " + next_word if next_word else ""}"
                    )

        # memoize the results for the current substring
        memo[remaining_str] = results
        return results

    return dfs(s, word_set, memoization)


def word_break_backtrack(s: str, word_dict: List[str]) -> List[str]:
    """
    This adds spaces to s to break it up into a sequence of valid words from word_dict.

    Uses backtracking to solve the problem.

    Args:
        s: The input string
        word_dict: The dictionary of words
    Returns:
        List of valid sentences
    """
    # convert word dict into a set for O(1) lookups
    word_set = set(word_dict)
    results = []

    def backtrack(
        sentence: str,
        words_set: Set[str],
        current_sentence: List[str],
        result: List[str],
        start_index: int,
    ):
        # If we've reached the end of the string, add the current sentence to results
        if start_index == len(sentence):
            result.append(" ".join(current_sentence))
            return

        # Iterate over possible end indices
        for end_index in range(start_index + 1, len(sentence) + 1):
            word = sentence[start_index:end_index]
            # If the word is in the set, proceed with backtracking
            if word in words_set:
                current_sentence.append(word)
                # Recursively call backtrack with the new end index
                backtrack(sentence, words_set, current_sentence, result, end_index)
                # Remove the last word to backtrack
                current_sentence.pop()

    backtrack(s, word_set, [], results, 0)
    return results
