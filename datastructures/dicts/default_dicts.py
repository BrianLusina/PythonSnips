"""
simple demo of creating default values in Python using defaultdict module. this allows to have
default values for newly added keys to a dictionary
"""
import random
from collections import defaultdict
from string import ascii_letters

# create an instance of default dict, which will return a dictionary with the default value for new
# keys having been created
d = defaultdict(list)

# call the key you want and you should get an empty list if the value does not yet exist
print(d["y"])  # []


def generate_values():
    """
    Simple 'generator' of values to a dictionary
    :return: dictionary with default values being set
    """
    result = defaultdict(list)
    for letter in ascii_letters:
        result[letter].append(random.choice(range(len(ascii_letters))))
    return result


if __name__ == "__main__":
    val = generate_values()
    print(val)
    # sample output
    # defaultdict(<class 'list'>, {'x': [1], 'f': [19], 'l': [34], 'P': [28], 'n': [9], 'v': [26], 'e': [36], 't': [38], 'I': [10], 'E': [40], 'O': [43], 'd': [27], 'G': [11], 'g': [35], 'K': [14], 'p': [6], 'Z': [39], 'h': [10], 'm': [31], 'Y': [31], 'S': [26], 'w': [7], 'y': [14], 'c': [49], 'A': [47], 'W': [38], 'N': [38], 'M': [5], 'R': [30], 'k': [48], 'o': [5], 'u': [21], 'L': [51], 'B': [37], 'U': [18], 'j': [23], 'D': [36], 'H': [4], 'r': [27], 'i': [16], 'F': [33], 'C': [26], 'a': [10], 'X': [7], 'b': [17], 'J': [19], 'V': [30], 'Q': [4], 'z': [49], 'T': [43], 'q': [21], 's': [42]})
