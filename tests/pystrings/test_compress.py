import unittest

from pystrings.compress import compress


class CompressStringTestCase(unittest.TestCase):
    def test_none(self):
        self.assertEqual(compress(None), None)

    def test_empty_string(self):
        self.assertEqual(compress(''), '')

    def test_no_need_to_compress(self):
        self.assertEqual(compress('AABBCC'), 'AABBCC')

    def test_compression_AAABCCDDDDE(self):
        self.assertEqual(compress('AAABCCDDDDE'), 'A3BC2D4E')

    def test_compression_BAAACCDDDD(self):
        self.assertEqual(compress('BAAACCDDDD'), 'BA3C2D4')

    def test_compression_AAABAACCDDDD(self):
        self.assertEqual(compress('AAABAACCDDDD'), 'A3BA2C2D4')


if __name__ == '__main__':
    unittest.main()
