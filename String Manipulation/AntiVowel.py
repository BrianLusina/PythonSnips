class AntiVowel(object):
    def __init__(self, text):
        self.text = text

    def anti_vowel(self):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vtext = ''.join(letter for letter in self.text if letter not in vowels)
        return vtext
