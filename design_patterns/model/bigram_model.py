from collections import defaultdict
from typing import Dict

from design_patterns.model.word_counter import WordCounter


class BigramModel:
    def __init__(self):
        self.next_word_counters: Dict[str, WordCounter] = defaultdict(WordCounter)

    def train(self, text: str):
        """
        For each word in the training dataset, build a WordCounter instance using all the words that follow it.
        """
        words = text.split()
        for i in range(len(words) - 1):
            word = words[i]
            next_word = words[i + 1] if i < len(words) - 1 else None
            if word not in self.next_word_counters:
                self.next_word_counters[word] = WordCounter()
            self.next_word_counters[word].update_count(next_word)

    def predict_next(self, word: str) -> str | None:
        """
        Predicts the next word that will follow the given word. Breaking ties randomly
        """
        if word not in self.next_word_counters:
            return None
        return self.next_word_counters[word].random_common_word()

    def generate(self, start: str, length: int) -> str:
        """
        Given a starting word and length, generate text by chaining predictions
        """
        result = [start]
        current_word = start
        for i in range(length - 1):
            next_word = self.predict_next(current_word)
            if next_word is None:
                break
            result.append(next_word)
            current_word = next_word

        return "".join(result)
