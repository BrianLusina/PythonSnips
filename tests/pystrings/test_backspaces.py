import unittest

from pystrings.backspaces import clean_string


class BackspacesTestCase(unittest.TestCase):

    def test_fixed(self):
        self.assertEqual(clean_string('abjd####jfk#'), "jf")
        self.assertEqual(clean_string('gfh#jds###d#dsd####dasdaskhj###dhkjs####df##s##d##'), "gdasda")
        self.assertEqual(clean_string('831####jns###s#cas/*####-5##s##6+yqw87e##hfklsd-=-28##fds##'),
                         "6+yqw8hfklsd-=-f")
        self.assertEquals(clean_string('######831###dhkj####jd#dsfsdnjkf###d####dasns'), "jdsfdasns")
        self.assertEquals(clean_string(''), "")
        self.assertEquals(clean_string('#######'), "")
        self.assertEquals(clean_string('####gfdsgf##hhs#dg####fjhsd###dbs########afns#######sdanfl##db#####s#a'), "sa")
        self.assertEquals(clean_string('#hskjdf#gd'), "hskjdgd")
        self.assertEquals(clean_string('hsk48hjjdfgd'), "hsk48hjjdfgd")

    def test_random(self):
        from random import randint, choice

        CHARS = [chr(i) for i in range(33, 126)] + ["#"] * 50

        for _ in range(50):
            s = "".join(choice(CHARS) for _ in range(randint(0, 25)))
            exp = []
            for c in s:
                if c == "#":
                    if exp:
                        exp.pop()
                else:
                    exp.append(c)
            exp = "".join(exp)

            self.assertEquals(clean_string(s), exp)


if __name__ == '__main__':
    unittest.main()
