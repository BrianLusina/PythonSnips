def verify(isbn):
    characters = list(isbn.replace("-", ""))
    if characters and characters[-1] == "X":
        characters[-1] = "10"

    if not len(characters) == 10 or not all(char.isdigit() for char in characters):
        return False

    indices = range(10, 0, -1)

    return sum(int(char) * index for char, index in zip(characters, indices)) % 11 == 0
