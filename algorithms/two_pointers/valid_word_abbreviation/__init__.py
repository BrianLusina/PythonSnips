def valid_word_abbreviation(word: str, abbr: str) -> bool:
    word_pointer = abbr_pointer = skip_count = 0
    word_len, abbr_len = len(word), len(abbr)

    while word_pointer < word_len and abbr_pointer < abbr_len:
        current_abbr_char = abbr[abbr_pointer]

        # Check for leading zeros: If abbr[abbr_pointer] == '0' and skip_count == 0, this is an invalid leading zero, return false
        if current_abbr_char.isdigit():
            if current_abbr_char == "0" and skip_count == 0:
                return False

            # Build the number: skip_count = skip_count * 10 + int(abbr[abbr_pointer]). This handles multi-digit numbers
            # like converting '1' followed by '0' into 10
            skip_count = skip_count * 10 + int(current_abbr_char)
        else:
            # Move the word pointer skip_count steps ahead along the word
            word_pointer += skip_count
            # Reset the skip count to 0
            skip_count = 0

            # boundary check and checking if the word pointer is pointing to the same character as the current abbreviation
            if word_pointer >= word_len or word[word_pointer] != current_abbr_char:
                return False

            # move to the next character in word
            word_pointer += 1

        # move to the next character in abbreviation
        abbr_pointer += 1

    return word_pointer + skip_count == word_len and abbr_pointer == abbr_len


def valid_word_abbreviation_2(word: str, abbr: str) -> bool:
    word_index, abbr_index = 0, 0

    while abbr_index < len(abbr):
        # Check if the current character is a digit.
        if abbr[abbr_index].isdigit():
            # Check if there's a leading zero. If there is, return False.
            if abbr[abbr_index] == "0":
                return False
            num = 0

            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])
                abbr_index += 1
            # Skip the number of characters in word as found in abbreviation.
            word_index += num
        else:
            # Check if characters the match, then increment the pointers. Otherwise return False.
            if word_index >= len(word) or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1

    # Check if both indices have reached the end of their respective strings.
    return word_index == len(word) and abbr_index == len(abbr)
