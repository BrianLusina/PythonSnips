import sys
from random import sample, randint, shuffle
from urllib import request

WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# get the words from the url and load into the list
for word in request.urlopen(WORD_URL):
    WORDS.append(word)


def convert(snippet, phrase):
    class_names = [w.capitalize for w in sample(WORDS, snippet.count("%%%"))]
    other_names = sample(WORDS, snippet.count("***"))
    results, param_names = [], []

    for i in range(0, snippet.count("@@@")):
        param_count = randint(1, 3)
        param_names.append(", ".join(sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # copies the list
        results = sentence[:]

        # fake class names
        for word in class_names:
            results = results.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            results = results.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            results = results.replace("@@@", word, 1)

        results.append(results)

    return results


# keep going until CTRL-D is hit

try:
    while True:
        snippets = PHRASES.keys()
        shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER:  %s\n\n" % answer)
except EOFError:
    print("\nBye")
