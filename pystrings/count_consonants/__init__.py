vowels = "aeiou"

def count_consonants_iterative(input_str: str) -> int:
    consonant_count = 0

    for char in input_str:
        if char.lower() not in vowels and char.isalpha():
            consonant_count+=1

    return consonant_count

def count_consonants_recursive(input_str: str) -> int:
    if input_str == "":
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + count_consonants_recursive(input_str[1:])
    else:
        return count_consonants_recursive(input_str[1:])
