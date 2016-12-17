import re


def order(sentence):
    result, word_list, c = [], sentence.split(), 0
    for word in word_list:
        if re.match(r"[a-zA-Z]+[1-9][a-zA-Z]+|^[1-9][a-zA-Z]+$|[a-zA-Z]+[1-9]$", word):
            for char in word:
                if char.isdigit():
                    digit = int(char)
                    print("Before:", word_list)
                    removed = word_list.pop(c)
                    print("After:", word_list)
                    word_list.insert(digit-1, word)
                    c += 1

    return " ".join(word_list)

# print("Actual: ", order("is2 Thi1s T4est 3a"), "Expected: ", "Thi1s is2 3a T4est")
print(order('Fo1r the2 g3ood th5e 4of pe6ople'), 'Fo1r the2 g3ood 4of th5e pe6ople')