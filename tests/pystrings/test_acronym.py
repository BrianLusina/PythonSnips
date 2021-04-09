import unittest

from pystrings.acronym_buster import acronym_buster


class AcronymTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(acronym_buster("BRB I need to go into a KPI meeting before EOD"), "BRB is an acronym. I do "
                                                                                           "not like acronyms. Please"
                                                                                           " remove them from your "
                                                                                           "email.")

    def test_2(self):
        self.assertEqual(acronym_buster("I am IAM so will be OOO until EOD"), "I am in a meeting so will be out of "
                                                                              "office until the end of the day")

    def test_3(self):
        self.assertEqual(acronym_buster("Going to WAH today. NRN. OOO"), "Going to work at home today. No reply "
                                                                         "necessary. Out of office")

    def test_4(self):
        self.assertEqual(acronym_buster("We're looking at SMB on SM DMs today"), "SMB is an acronym. I do not like "
                                                                                 "acronyms. Please remove them from "
                                                                                 "your email.")

    def test_5(self):
        self.assertEqual(acronym_buster("OOO"), "Out of office")

    def test_6(self):
        self.assertEqual(acronym_buster("KPI"), "Key performance indicators")

    def test_7(self):
        self.assertEqual(acronym_buster("EOD"), "The end of the day")

    def test_8(self):
        self.assertEqual(acronym_buster("TBD"), "To be decided")

    def test_9(self):
        self.assertEqual(acronym_buster("TBD by EOD"), "To be decided by the end of the day")

    def test_10(self):
        self.assertEqual(acronym_buster("BRB I am OOO"), "BRB is an acronym. I do not like acronyms. Please remove "
                                                         "them from your email.")

    def test_11(self):
        self.assertEqual(acronym_buster("WAH"), "Work at home")

    def test_12(self):
        self.assertEqual(acronym_buster("IAM"), "In a meeting")

    def test_13(self):
        self.assertEqual(acronym_buster("NRN"), "No reply necessary")

    def test_14(self):
        self.assertEqual(acronym_buster("CTA"), "Call to action")

    def test_15(self):
        self.assertEqual(acronym_buster("Hi PAB"), "PAB is an acronym. I do not like acronyms. Please remove them "
                                                   "from your email.")

    def test_16(self):
        self.assertEqual(acronym_buster("HATDBEA"), "HATDBEA is an acronym. I do not like acronyms. Please remove "
                                                    "them from your email.")

    def test_17(self):
        self.assertEqual(acronym_buster("LDS"), "LDS is an acronym. I do not like acronyms. Please remove them from "
                                                "your email.")

    def test_18(self):
        self.assertEqual(acronym_buster("PB"), "PB")

    def test_19(self):
        self.assertEqual(acronym_buster("FA"), "FA")

    def test_20(self):
        self.assertEqual(acronym_buster("CTA and HTTP"), "HTTP is an acronym. I do not like acronyms. Please remove "
                                                         "them from your email.")

    def test_21(self):
        self.assertEqual(acronym_buster("SWOT."), "Strengths, weaknesses, opportunities and threats.")

    def test_22(self):
        self.assertEqual(acronym_buster("HTTP"), "HTTP is an acronym. I do not like acronyms. Please remove them from "
                                                 "your email.")

    def test_23(self):
        self.assertEqual(acronym_buster("Please WAH today. KPI on track"), "Please work at home today. Key "
                                                                           "performance indicators on track")

    def test_24(self):
        self.assertEqual(acronym_buster("The advert needs a CTA. NRN before EOD."), "The advert needs a call to "
                                                                                    "action. No reply necessary "
                                                                                    "before the end of the day.")

    def test_25(self):
        self.assertEqual(acronym_buster("I sent you a RFP yesterday."), "RFP is an acronym. I do not like acronyms. "
                                                                        "Please remove them from your email.")

    def test_26(self):
        self.assertEqual(acronym_buster("My SM account needs some work."), "My SM account needs some work.")


if __name__ == '__main__':
    unittest.main()
