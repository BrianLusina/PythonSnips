from typing import Generator, Any
from itertools import zip_longest


def backspace_compare_two_pointers(s: str, t: str) -> bool:
    def f(word: str) -> Generator[str, Any, None]:
        skip = 0
        for x in reversed(word):
            if x == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all(x == y for x, y in zip_longest(f(s), f(t)))


def backspace_compare_two_pointers_2(s: str, t: str) -> bool:
    # Initialize pointers at the end of each string
    pointer_s, pointer_t = len(s) - 1, len(t) - 1
    # Track pending backspaces for each string
    skip_s, skip_t = 0, 0

    # Continue while there are characters left to process in either string
    while pointer_s >= 0 or pointer_t >= 0:
        # Advance pointer in s to find the next valid character
        while pointer_s >= 0:
            if s[pointer_s] == "#":
                # Increment skip count and move pointer left
                skip_s += 1
                pointer_s -= 1
            elif skip_s > 0:
                # This character is cancelled by a backspace; consume skip and move left
                skip_s -= 1
                pointer_s -= 1
            else:
                # Found a valid character in s
                break

        # Advance pointer in t to find the next valid character
        while pointer_t >= 0:
            if t[pointer_t] == "#":
                # Increment skip count and move pointer left
                skip_t += 1
                pointer_t -= 1
            elif skip_t > 0:
                # This character is cancelled by a backspace; consume skip and move left
                skip_t -= 1
                pointer_t -= 1
            else:
                # Found a valid character in t
                break

        # Compare the current valid characters from both strings
        if pointer_s >= 0 and pointer_t >= 0:
            # If characters differ, strings are not equal
            if s[pointer_s] != t[pointer_t]:
                return False
        elif pointer_s >= 0 or pointer_t >= 0:
            # One string has characters remaining while the other is exhausted
            return False

        # Move both pointers left to continue comparison
        pointer_s -= 1
        pointer_t -= 1

    # All characters matched
    return True


def backspace_compare_build_string(s: str, t: str) -> bool:
    def build(word: str) -> str:
        ans = []
        for c in word:
            if c != "#":
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)

    return build(s) == build(t)
