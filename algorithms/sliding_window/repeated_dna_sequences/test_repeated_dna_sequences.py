import unittest
from . import find_repeated_dna_sequences, find_repeated_dna_sequences_naive


class FindRepeatedDnaSequencesTestCase(unittest.TestCase):
    def test_1(self):
        dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected = ["CCCCCAAAAA", "AAAAACCCCC"]
        actual = find_repeated_dna_sequences(dna_sequence)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_2(self):
        dna_sequence = "GGGGGGGGGGGGGGGGGGGG"
        expected = ["GGGGGGGGGG"]
        actual = find_repeated_dna_sequences(dna_sequence)
        self.assertEqual(expected, actual)

    def test_3(self):
        dna_sequence = "TTTGGGAAATTTGGGAAACC"
        expected = []
        actual = find_repeated_dna_sequences(dna_sequence)
        self.assertEqual(expected, actual)

    def test_4(self):
        dna_sequence = "AAAAAAAAAAAAA"
        expected = ["AAAAAAAAAA"]
        actual = find_repeated_dna_sequences(dna_sequence)
        self.assertEqual(expected, actual)

    def test_5(self):
        dna_sequence = "ACGTACGTACGTACGTACGTACGTACGTACGT"
        expected = ["ACGTACGTAC", "CGTACGTACG", "GTACGTACGT", "TACGTACGTA"]
        actual = find_repeated_dna_sequences(dna_sequence)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_6(self):
        dna_sequence = "GTACGTACGTACGCCCCCCCCGGGGG"
        expected = []
        actual = find_repeated_dna_sequences(dna_sequence)
        self.assertEqual(expected, actual)


class FindRepeatedDnaSequencesNaiveTestCase(unittest.TestCase):
    def test_1(self):
        dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected = ["CCCCCAAAAA", "AAAAACCCCC"]
        actual = find_repeated_dna_sequences_naive(dna_sequence)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_2(self):
        dna_sequence = "GGGGGGGGGGGGGGGGGGGG"
        expected = ["GGGGGGGGGG"]
        actual = find_repeated_dna_sequences_naive(dna_sequence)
        self.assertEqual(expected, actual)

    def test_3(self):
        dna_sequence = "TTTGGGAAATTTGGGAAACC"
        expected = []
        actual = find_repeated_dna_sequences_naive(dna_sequence)
        self.assertEqual(expected, actual)

    def test_4(self):
        dna_sequence = "AAAAAAAAAAAAA"
        expected = ["AAAAAAAAAA"]
        actual = find_repeated_dna_sequences_naive(dna_sequence)
        self.assertEqual(expected, actual)

    def test_5(self):
        dna_sequence = "ACGTACGTACGTACGTACGTACGTACGTACGT"
        expected = ["ACGTACGTAC", "CGTACGTACG", "GTACGTACGT", "TACGTACGTA"]
        actual = find_repeated_dna_sequences_naive(dna_sequence)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_6(self):
        dna_sequence = "GTACGTACGTACGCCCCCCCCGGGGG"
        expected = []
        actual = find_repeated_dna_sequences_naive(dna_sequence)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
