import unittest

from algorithms.get_user_id import get_users_ids


class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_users_ids("uid12345"), ["12345"])

    def test2(self):
        self.assertEqual(get_users_ids("   uidabc  "), ["abc"])

    def test3(self):
        self.assertEqual(get_users_ids("#uidswagger"), ["swagger"])

    def test4(self):
        self.assertEqual(get_users_ids("uidone,uidtwo"), ["one", "two"])

    def test5(self):
        self.assertEqual(get_users_ids("uidCAPSLOCK"), ["capslock"])

    def test6(self):
        self.assertEqual(get_users_ids("uid##doublehashtag"), ["doublehashtag"])

    def test7(self):
        self.assertEqual(get_users_ids("  uidin name whitespace"), ["in", "name", "whitespace"])

    def test8(self):
        self.assertEqual(get_users_ids("uidMultipleuid"), ["multipleuid"])

    @unittest.skip
    def test9(self):
        self.assertEqual(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), ["12 ab", "", "mixedchars"])

    def test10(self):
        self.assertEqual(get_users_ids(" uidT#e#S#t# "), ["test"])
