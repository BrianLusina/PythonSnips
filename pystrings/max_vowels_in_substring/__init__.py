def max_vowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    current_max_vowels = max_len = 0

    for x in range(len(s)):
        current_max_vowels += s[x] in vowels
        if x >= k:
            current_max_vowels -= s[x - k] in vowels

        max_len = max(current_max_vowels, max_len)

    return max_len
