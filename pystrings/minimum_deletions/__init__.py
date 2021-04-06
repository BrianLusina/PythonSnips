from collections import Counter


def minimum_deletions(word: str) -> int:
    counter = Counter(word)
    deletions = 0

    counts = [x for x in counter.values()]

    for x in range(len(counts)):
        for y in range(x + 1, len(counts)):
            if counts[x] > 0 and counts[x] == counts[y]:
                count = counts[y]
                counts[y] = count - 1
                deletions += 1
            else:
                break

    return deletions


def min_deletions(s: str) -> int:
    count, result, used = Counter(s), 0, set()

    for character, frequency in count.items():

        while frequency > 0 and frequency in used:
            frequency -= 1
            result += 1

        used.add(frequency)

    return result
