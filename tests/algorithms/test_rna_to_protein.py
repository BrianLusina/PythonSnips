import unittest

from algorithms.rna_to_protein import protein


class RnaTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(protein("AUGUGA"), "M")

    def test2(self):
        self.assertEqual(protein("AUG"), "M")

    def test3(self):
        self.assertEqual(protein("AUGGUUAGUUGA"), "MVS")

    def test4(self):
        self.assertEqual(protein("UGCGAUGAAUGGGCUCGCUCC"), "CDEWARS")

    def test5(self):
        self.assertEqual(
            protein("AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA"), "MSFHQGNHARSAF"
        )

    def test6(self):
        self.assertEqual(
            protein("AUGCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAGUUGA"), "MLQVHWKRRGKTS"
        )

    def test7(self):
        self.assertEqual(
            protein("AUGGCGUUCAGCUUUCUAUGGAGGGUAGUGUACCCAUGCUGA"), "MAFSFLWRVVYPC"
        )

    def test8(self):
        self.assertEqual(
            protein("AUGCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUGA"), "MQLSMEGSVNYHA"
        )

    def test9(self):
        self.assertEqual(
            protein("AUGCUAUGGAGGGUAGUGUUAACUACCACGCCCAGUACUUGA"), "MLWRVVLTTTPST"
        )

    def test10(self):
        self.assertEqual(
            protein(
                "AUGUAUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAUACGAAGGCACCCAAAGCCUGAAUAUUACAAUAACUGAAGGAGGUCCUCUGCCAUUUGCUUUUGACAUUCUGUCACACGCCUUUCAGUAUGGCAUCAAGGUCUUCGCCAAGUACCCCAAAGAAAUUCCUGACUUCUUUAAGCAGUCUCUACCUGGUGGUUUUUCUUGGGAAAGAGUAAGCACCUAUGAAGAUGGAGGAGUGCUUUCAGCUACCCAAGAAACAAGUUUGCAGGGUGAUUGCAUCAUCUGCAAAGUUAAAGUCCUUGGCACCAAUUUUCCCGCAAACGGUCCAGUGAUGCAAAAGAAGACCUGUGGAUGGGAGCCAUCAACUGAAACAGUCAUCCCACGAGAUGGUGGACUUCUGCUUCGCGAUACCCCCGCACUUAUGCUGGCUGACGGAGGUCAUCUUUCUUGCUUCAUGGAAACAACUUACAAGUCGAAGAAAGAGGUAAAGCUUCCAGAACUUCACUUUCAUCAUUUGCGUAUGGAAAAGCUGAACAUAAGUGACGAUUGGAAGACCGUUGAGCAGCACGAGUCUGUGGUGGCUAGCUACUCCCAAGUGCCUUCGAAAUUAGGACAUAACUGA"
            ),
            "MYPSIKETMRVQLSMEGSVNYHAFKCTGKGEGKPYEGTQSLNITITEGGPLPFAFDILSHAFQYGIKVFAKYPKEIPDFFKQSLPGGFSWERVSTYEDGGVLSATQETSLQGDCIICKVKVLGTNFPANGPVMQKKTCGWEPSTETVIPRDGGLLLRDTPALMLADGGHLSCFMETTYKSKKEVKLPELHFHHLRMEKLNISDDWKTVEQHESVVASYSQVPSKLGHN",
            "This gene encodes for a protein that fluoresces green in the Snakelocks anemone!",
        )
