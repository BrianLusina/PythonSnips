class Censor(object):
    def __init__(self, text, word):
        self.word = word
        self.text = text

    def censor(self):
        string_list = self.text.split()
        new_list = []
        new_sent = ""
        for w in string_list:
            if w == self.word:
                new_list.append("*" * len(self.word))
            else:
                new_list.append(w)

            new_sent = " ".join(new_list)
        return new_sent
