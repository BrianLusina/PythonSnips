from typing import List


def reverse_words(message: str) -> str:
    message_list = list(" ".join(message.strip().split()))

    # first we reverse all the characters in the entire message_list
    reverse_characters(message_list, 0, len(message_list) - 1)
    # this gives us the right word order
    # but with each word backwards

    # now we'll make the words forward again
    # by reversing each word's characters

    # we hold the index of the /start/ of the current word
    # as we look for the /end/ of the current word
    current_word_start_index = 0

    for i in range(len(message_list) + 1):
        # found the end of the current word!
        if (i == len(message_list)) or (message_list[i] == " "):
            reverse_characters(message_list, current_word_start_index, i - 1)

            # if we haven't exhausted the string our
            # next word's start is one character ahead
            current_word_start_index = i + 1

    return "".join(message_list)


def reverse_characters(message_list: List[str], front_index: int, back_index: int):
    # walk towards the middle, from both sides
    while front_index < back_index:
        # swap the front char and back char
        message_list[front_index], message_list[back_index] = (
            message_list[back_index],
            message_list[front_index],
        )

        front_index += 1
        back_index -= 1

    return message_list


def reverse_words_two_pointers(sentence: str) -> str:
    result = sentence.split()
    left = 0
    right = len(result) - 1
    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return " ".join(result)
