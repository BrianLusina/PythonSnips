from string import ascii_lowercase


def destroyer(input_sets):
    letters_to_knock = []
    for sets in input_sets:
        for char in sets:
            letters_to_knock.append(char)

