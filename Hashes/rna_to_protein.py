import unittest, re

AMINO_DICT = {
    # Phenylalanine
    'UUC': 'F', 'UUU': 'F',
    # Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Methionine
    'AUG': 'M',
    # Valine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine
    'UAU': 'Y', 'UAC': 'Y',
    # Histidine
    'CAU': 'H', 'CAC': 'H',
    # Glutamine
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine
    'AAU': 'N', 'AAC': 'N',
    # Lysine
    'AAA': 'K', 'AAG': 'K',
    # Aspartic Acid
    'GAU': 'D', 'GAC': 'D',
    # Glutamic Acid
    'GAA': 'E', 'GAG': 'E',
    # Cystine
    'UGU': 'C', 'UGC': 'C',
    # Tryptophan
    'UGG': 'W',
    # Arginine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # Stop codon
    'UAA': 'Stop', 'UGA': 'Stop', 'UAG': 'Stop'
}

"""
Split the string into parts of 3,
perform a for loop, checking through each key in dictionary, checking if the parts of three are in the key,
 if so, add to a string and continue the search
"""


def protein(rna):
    prot_result = ""
    rna_splits = re.split(r'([A-Z]{3})', rna)


class RnaTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(protein('AUGUGA'), 'M')

    def test2(self):
        self.assertEqual(protein('AUG'), 'M')

    def test3(self):
        self.assertEqual(protein('AUGGUUAGUUGA'), 'MVS')

    def test4(self):
        self.assertEqual(protein('UGCGAUGAAUGGGCUCGCUCC'), 'CDEWARS')

    def test5(self):
        self.assertEqual(protein('AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA'), 'MSFHQGNHARSAF')

    def test6(self):
        self.assertEqual(protein('AUGCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAGUUGA'), 'MLQVHWKRRGKTS')

    def test7(self):
        self.assertEqual(protein('AUGGCGUUCAGCUUUCUAUGGAGGGUAGUGUACCCAUGCUGA'), 'MAFSFLWRVVYPC')

    def test8(self):
        self.assertEqual(protein('AUGCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUGA'), 'MQLSMEGSVNYHA')

    def test9(self):
        self.assertEqual(protein('AUGCUAUGGAGGGUAGUGUUAACUACCACGCCCAGUACUUGA'), 'MLWRVVLTTTPST')

    def test10(self):
        self.assertEqual(protein('AUGUAUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAUACGAAGGCACCCAAAGCCUGAAUAUUACAAUAACUGAAGGAGGUCCUCUGCCAUUUGCUUUUGACAUUCUGUCACACGCCUUUCAGUAUGGCAUCAAGGUCUUCGCCAAGUACCCCAAAGAAAUUCCUGACUUCUUUAAGCAGUCUCUACCUGGUGGUUUUUCUUGGGAAAGAGUAAGCACCUAUGAAGAUGGAGGAGUGCUUUCAGCUACCCAAGAAACAAGUUUGCAGGGUGAUUGCAUCAUCUGCAAAGUUAAAGUCCUUGGCACCAAUUUUCCCGCAAACGGUCCAGUGAUGCAAAAGAAGACCUGUGGAUGGGAGCCAUCAACUGAAACAGUCAUCCCACGAGAUGGUGGACUUCUGCUUCGCGAUACCCCCGCACUUAUGCUGGCUGACGGAGGUCAUCUUUCUUGCUUCAUGGAAACAACUUACAAGUCGAAGAAAGAGGUAAAGCUUCCAGAACUUCACUUUCAUCAUUUGCGUAUGGAAAAGCUGAACAUAAGUGACGAUUGGAAGACCGUUGAGCAGCACGAGUCUGUGGUGGCUAGCUACUCCCAAGUGCCUUCGAAAUUAGGACAUAACUGA'),'MYPSIKETMRVQLSMEGSVNYHAFKCTGKGEGKPYEGTQSLNITITEGGPLPFAFDILSHAFQYGIKVFAKYPKEIPDFFKQSLPGGFSWERVSTYEDGGVLSATQETSLQGDCIICKVKVLGTNFPANGPVMQKKTCGWEPSTETVIPRDGGLLLRDTPALMLADGGHLSCFMETTYKSKKEVKLPELHFHHLRMEKLNISDDWKTVEQHESVVASYSQVPSKLGHN','This gene encodes for a protein that fluoresces green in the Snakelocks anemone!')
