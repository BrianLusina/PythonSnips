from collections import Counter


def minDeletions(s: str) -> int:
    count, result, used = Counter(s), 0, set()

    for _, frequency in count.items():

        while frequency > 0 and frequency in used:
            frequency -= 1
            result += 1

        used.add(frequency)

    return result
