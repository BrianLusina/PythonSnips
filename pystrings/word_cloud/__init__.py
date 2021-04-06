words_to_counts = {}


class WordCloudData:
    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        """
        Iterates over each character in the input string, splitting
        words and passing them to add_word_to_dictionary
        :param: input_string
        """
        current_word_start_index = 0
        current_word_length = 0

        for i, character in enumerate(input_string):

            # if we reacched the end of the string, we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                                                current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)

            # if we reach a space or emdash, we know we are at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == " " or character == u'\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                                                current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            # we want to make sure we split an ellipses so it we get 2 periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == ".":
                if i < len(input_string) - 1 and input_string[i + 1] == ".":
                    if current_word_length > 0:
                        current_wrd = input_string[current_word_start_index:
                                                   current_word_start_index + current_word_length]
                        self.add_word_to_dictionary[current_word]
                        current_word_length = 0

            # if the character is a letter of an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            # if the character is a hyphen, we want to check if it's surrounded by letters
            # if it is we add it to our current word
            elif character == "-":
                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    if current_word_length == 0:
                        current_word_start_index = i
                    current_word_length += 1

                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                                                    current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

    def add_word_to_dictionary(self, word):
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they are always uppercase, so we just increment
        # the lowercase version count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # if an uppercase version is in the dictionary, we know our input word must be lowercase
        # since we only include uppercase words if they're always uppercase, we add the lowercase
        # version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so, we add it to the dictionary
        else:
            self.words_to_counts[word] = 1
