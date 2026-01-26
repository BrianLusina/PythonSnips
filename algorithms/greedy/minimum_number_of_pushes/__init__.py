from collections import Counter
import heapq


def minimum_pushes_greedy_with_sorting(word: str) -> int:
    # frequency vector of size 26 that storees the count of each letter in the word
    # Space complexity here is O(1) because we have a constant space for the given list, i.e. 26
    frequency = [0] * 26

    # Iterate throuch each character and increment the count in the frequency at the index corresponding to char - "a"
    # since we know from the given constraints that we will have lowercase English letters, this will work fine
    # This is an O(n) operation, as each character in the word is iterated through
    for char in word:
        frequency[ord(char) - ord("a")] += 1

    # Sort the frequencies in descending order to prioritize letters with higher counts
    # O(n log(n)) operation to handle sorting, with a space complexity of O(n) as Python uses in-memory space to handle
    # the sorting using timsort
    frequency.sort(reverse=True)

    # total number of key presses required
    total_pushes = 0

    # iterate through the sorted frequency
    for i in range(26):
        # if the frequency of a letter is zero, break the loop as there are no more letters to process
        if frequency[i] == 0:
            break
        # calculate the number of pushes for each letter based on its position in the sorted list (i / 8 + 1) * frequency[i]
        total_pushes += (i // 8 + 1) * frequency[i]

    return total_pushes


def minimum_pushes_heap(word: str) -> int:
    # frequency_map to store the count of each letter
    frequency_map = Counter(word)

    # Priority queue/max heap to store frequencies in descending order
    frequency_queue = [-freq for freq in frequency_map.values()]
    heapq.heapify(frequency_queue)

    # total number of key presses required
    total_pushes = 0
    index = 0

    # iterate through the sorted frequency_map
    while frequency_queue:
        total_pushes += (1 + (index // 8)) * -heapq.heappop(frequency_queue)
        index += 1

    return total_pushes
