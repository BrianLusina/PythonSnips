from random import randrange


class WordCounter:
    """
    Counts the number of times each word appears in a dataset.
    """

    def __init__(self):
        """
        Set up an empty dictionary of word:count pairs.
        """
        self.counts = {}

    def update_count(self, word):
        """
        Given a word from the dataset, update its count.
        """
        if word in self.counts:
            self.counts[word] += 1
        else:
            self.counts[word] = 1

    def get_count(self, word):
        """
        Return the number of times a word appears in the dataset.
        """
        return self.counts.get(word, 0)

    def in_dataset(self, word):
        """
        Return whether a word is in the dataset.
        """
        return word in self.counts

    def distinct_words(self):
        """
        Return the number of distinct words in the dataset.
        """
        return len(self.counts)

    def total_words(self):
        """
        Return the total number of words in the dataset.
        """
        total = 0

        for word in self.counts:
            total += self.counts[word]

        return total

    def count_data(self, text):
        """
        Count all the words in a text string.
        """
        words = text.split()
        for word in words:
            self.update_count(word)

    def greatest_count(self):
        """
        Return the highest word count in the dataset.
        """
        greatest = 0
        for word in self.counts:
            word_count = self.get_count(word)

            if word_count > greatest:
                greatest = word_count
        return greatest

    def most_common_words(self):
        """
        Return a list of the most common words.
        """
        most_common = []
        max_count = self.greatest_count()

        for word in self.counts:
            word_count = self.get_count(word)
            if word_count == max_count:
                most_common.append(word)
        return most_common

    def random_common_word(self):
        """
        Return one of the most common words at random.
        """
        common_list = self.most_common_words()
        choice = randrange(len(common_list))
        return common_list[choice]
