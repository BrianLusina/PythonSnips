from unittest import TestCase
from pysnips.strings_words.generate_user_links import generate_link


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
        self.assertEqual(generate_link("io819`p[u& )}|n~*q$f+yej.v,5rc;^z%w: "),
                         self.base_url + 'io819%60p%5Bu%26%20%29%7D%7Cn%7E%2Aq%24f%2Byej.v%2C5rc%3B%5Ez%25w')

    def test_8(self):
        self.assertEqual(generate_link("fsn/30d8cg<2"), self.base_url + "fsn/30d8cg%3C2")

    def test_9(self):
        self.assertEqual(generate_link('g)8"a}3mvx0_1s4b+?.&2(pe|>;@~6 z^`kc<o!$i:7,#*{u)'),
                         self.base_url + "g%298%22a%7D3mvx0_1s4b%2B%3F.%262%28pe%7C%3E%3B%40%7E6%20z%5E%60kc%3Co%21%24i%3A7%2C%23%2A%7Bu")

    def test_10(self):
        self.assertEqual(generate_link('.nyh1c"u>s,_<8\0m`(b52a$kio|_#:@+'),
                         self.base_url + '.nyh1c%22u%3Es%2C_%3C8%5C0m%60%28b52a%24kio%7C_%23%3A%40%2B')
