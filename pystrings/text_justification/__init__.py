from typing import List


def full_justify(words: List[str], max_width: int) -> List[str]:
    """
    How does it work? This uses a round-robin. The following line implements the round-robin logic:
    for i in range(maxWidth - num_of_letters):
        cur[i%(len(cur)-1 or 1)] += ' '

    What does this line do? Once you determine that there are only k words that can fit on a given line, you know what
    the total length of those words is num_of_letters. Then the rest are spaces, and there are
    (max_width - num_of_letters) of spaces. The "or 1" part is for dealing with the edge case len(cur) == 1.

    Args:
        words (list): words to fully justify
        max_width (int): width of each line
    Returns:
         list: list of justified words
    """
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(max_width)]
