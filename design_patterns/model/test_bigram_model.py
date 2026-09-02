import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from design_patterns.model.bigram_model import BigramModel
from design_patterns.model.word_counter import WordCounter

BIGRAM_MODEL_TRAIN_TEST_CASES = [
    (
        "hey my kitten my kitten and hey my kitten my deary",
        {
            "hey": WordCounter(),
            "my": WordCounter(),
        },
    ),
]


class BigramModelTestCase(unittest.TestCase):
    @parameterized.expand(
        BIGRAM_MODEL_TRAIN_TEST_CASES, name_func=custom_test_name_func
    )
    def test_train_model(self, text: str, expected: str):
        bigram_model = BigramModel()
        bigram_model.train(text)
        self.assertEqual(True, False)  # add assertion here

    # @parameterized.expand(BIGRAM_MODEL_TRAIN_TEST_CASES, name_func=custom_test_name_func)
    def test_predict_next_word(wself):
        text = "hey my kitten my kitten and hey my kitten my deary"
        bigram_model = BigramModel()
        bigram_model.train(text)
        actual = bigram_model.predict_next("pizza")
        expected = None
        self.assertEqual(expected, actual)

    def test_generate_words(self):
        text = (
            "if all the seas were one sea "
            "what a great sea that would be "
            "and if all the trees were one tree "
            "what a great tree that would be "
            "and if all the axes were one axe "
            "what a great axe that would be "
            "and if all the men were one man "
            "what a great man he would be "
            "and if the great man took the great axe "
            "and cut down the great tree "
            "and let it fall into the great sea "
            "what a splish splash that would be"
        )
        bigram_model = BigramModel()
        bigram_model.train(text)
        actual = bigram_model.generate("the", 10)
        print(actual)

        self.assertIsNotNone(actual)


if __name__ == "__main__":
    unittest.main()
