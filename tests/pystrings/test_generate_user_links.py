from unittest import TestCase

from pystrings.generate_user_links import generate_link


class GenerateUserLinksTests(TestCase):
    base_url = "http://www.codewars.com/users/"

    def test_1(self):
        self.assertEqual(generate_link('matt c'), self.base_url + 'matt%20c')

    def test_2(self):
        self.assertEqual(generate_link('matt c'), self.base_url + 'matt%20c')

    def test_3(self):
        self.assertEqual(generate_link('g964'), self.base_url + 'g964')

    def test_4(self):
        self.assertEqual(generate_link('GiacomoSorbi'), self.base_url + 'GiacomoSorbi')

    def test_5(self):
        self.assertEqual(generate_link('ZozoFouchtra'), self.base_url + 'ZozoFouchtra')

    def test_6(self):
        self.assertEqual(generate_link('colbydauph'), self.base_url + 'colbydauph')

    def test_7(self):
        self.assertEqual(generate_link("fsn/30d8cg<2"), self.base_url + "fsn/30d8cg%3C2")
