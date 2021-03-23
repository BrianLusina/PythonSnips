class RemoveDuplicate(object):
    def __init__(self, strin):
        self.strin = strin

    def remove_duplicate(self):
        """
        split the string to obtain individual word elements, remove duplicate words
        for each word
        loop through characters in string and check if it is not in output string
        if not, add to output string, return the string.
        """
        out = []
        for x in self.strin.lower():
            if x not in out:
                out.append(x)
        return "".join(out)


class RemoveDupSort(object):
    def __init__(self, sentence):
        self.sentence = sentence

    def remover(self):
        words = self.sentence.split(" ")
        return " ".join(sorted(set(words)))
