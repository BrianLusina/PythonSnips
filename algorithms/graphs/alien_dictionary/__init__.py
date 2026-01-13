from typing import Deque, DefaultDict, List, Counter, Set
from collections import defaultdict, Counter, deque


def alien_order(words: List[str]) -> str:
    word_length = len(words)
    # Edge cases where the length of the list is 0 and 1. If 0, return an empty string
    if word_length == 0:
        return ""

    # Graph will store the graph representation of the letters using a dictionary where the key will be a letter and the
    # value will be a list representing the neighbors of the key. So, we can move from, say, a to b or c if the graph is
    # {a: [b, c]}
    graph: DefaultDict[str, Set[str]] = defaultdict(set)

    # This is used to store the number of edges that are incoming to a given node(letter). 0 is default indicating that
    # the letter is possibly, the first in the alphabet, based on what order we find from the given list of words.
    in_degree: DefaultDict[str, int] = defaultdict(lambda: 0)

    # set every unique character in every word in words to 0
    for word in words:
        for char in word:
            if not in_degree[char]:
                in_degree[char] = 0

    # Compare the orderings of letters in the supplied words. The comparison is done two words at a time, where the differing
    # character between the words is used to determine the ordering of the letters. so, if two words are 'abc' and 'adbc', we
    # only check 'b' and 'd'. Since abc comes before adbc, we can conclude that 'b' comes before 'd' and we end the
    # comparison there and move to the next two words to compare and do the same matching
    for idx in range(word_length - 1):
        current_word = words[idx]
        next_word = words[idx + 1]
        current_word_len = len(current_word)
        next_word_len = len(next_word)

        # Prefix check, if the current word is longer than the next word and prefix is a prefix of current word, then return
        # ane empty string as that indicates an invalid ordering
        if current_word_len > next_word_len and current_word.startswith(next_word):
            return ""

        # Check for the differing character in the two words. If the characters differ, the character from the current
        # word comes before the character from the next word
        for i in range(min(current_word_len, next_word_len)):
            char_one = current_word[i]
            char_two = next_word[i]
            # these are the same characters, so, we move to the next two characters to compare
            if char_one != char_two:
                # Only increment in_degree if this is a new directed edge
                if char_two not in graph[char_one]:
                    graph[char_one].add(char_two)
                    # Character two will have an indegree where we increment it by 1, because we can move from character one
                    # to character two
                    in_degree[char_two] += 1
                # We don't need to compare the next two characters at this point
                break

    # Queue which we will be popping of characters to create a valid alien word from. This will contain all the characters
    # with an indegree of 0 initially
    queue: Deque[str] = deque([i for i in in_degree if in_degree[i] == 0])

    # The final word we can create
    word = ""

    while queue:
        character = queue.popleft()
        word += character

        for next_character in graph[character]:
            in_degree[next_character] -= 1
            if in_degree[next_character] == 0:
                queue.append(next_character)

    return "" if len(word) < len(in_degree.keys()) else word


def alien_order_2(words: List[str]) -> str:
    adj_list: DefaultDict[str, Set[str]] = defaultdict(set)
    counts: Counter[str] = Counter({c: 0 for word in words for c in word})

    for word1, word2 in zip(words, words[1:]):
        for c, d in zip(word1, word2):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break

        else:
            if len(word2) < len(word1):
                return ""

    result: List[str] = []
    sources_queue: Deque[str] = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)

        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)

    if len(result) < len(counts):
        return ""
    return "".join(result)
