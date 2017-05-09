class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()

        current_word = ''
        for i, character in enumerate(input_string):

            # if we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string)-1:
                if character.isalpha():
                    current_word += character
                if current_word: 
                    self.add_word_to_dictionary(current_word)

            # if we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word:
                    self.add_word_to_dictionary(current_word)
                current_word = ''

            # we want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string)-1 and input_string[i+1] == '.':
                    if current_word: 
                        self.add_word_to_dictionary(current_word)
                    current_word = ''

            # if the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                current_word += character

            # if the character is a hyphen, we want to check if it's surrounded by letters
            # if it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i-1].isalpha() and \
                        input_string[i+1].isalpha():
                    current_word += character

    def add_word_to_dictionary(self, word):

        # if the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # if an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1

