def find_rotation_point(words):
    first_word = words[0]

    floor_index = 0

    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:

        # guess a point 1/2 way between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        # if guess comes after the first word or is the first word
        if words[guess_index] >= first_word:
            # go right
            floor_index = guess_index
        else:
            # go left
            ceiling_index = guess_index

        # if floor and ceiling have changed
        if floor_index + 1 == ceiling_index:
            # between the floor and ceiling is where we flipped to the beginning 
            return ceiling_index
