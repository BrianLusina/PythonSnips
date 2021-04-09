import unittest

from pyregex.file_extensions import is_img, is_audio


class FileExtTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_audio("Nothing Else Matters.mp3"), False)

    def test_2(self):
        self.assertEqual(is_audio("NothingElseMatters.mp3"), True)

    def test_3(self):
        self.assertEqual(is_audio("DaftPunk.FLAC"), False)

    def test_4(self):
        self.assertEqual(is_audio("DaftPunk.flac"), True)

    def test_5(self):
        self.assertEqual(is_audio("AmonTobin.aac"), True)

    def test_6(self):
        self.assertEqual(is_audio(" Amon Tobin.alac"), False)

    def test_7(self):
        self.assertEqual(is_audio("tobin.alac"), True)

    def test_8(self):
        self.assertEqual(is_img("Home.jpg"), True)

    def test_9(self):
        self.assertEqual(is_img("flat.jpeg"), True)

    def test_10(self):
        self.assertEqual(is_img("icon.bmp"), True)

    def test_11(self):
        self.assertEqual(is_img("icon2.jpg"), False)

    def test_12(self):
        self.assertEqual(is_img("bounce.gif"), True)

    def test_13(self):
        self.assertEqual(is_img("animate bounce.GIF"), False)

    def test_14(self):
        self.assertEqual(is_img("transparency.png"), True)


if __name__ == '__main__':
    unittest.main()
