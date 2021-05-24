import unittest
from random import choice, randint

from algorithms.strings.validate_ip import is_valid_ipv4

test_tuple = (
    ('', 'abc.def.ghi.jkl', '123.456.789.0', '12.34.56', '123.045.067.089',
     '256.1.2.3', '1.2.3.4.5', '123,45,67,89', ' 1.2.3.4', '1.2.3.4 ', '12.34.56.-1'),
    tuple('.'.join([str(randint(0, 255)) for iwqeouqre98 in range(4)]) for weuiwq28318 in range(18))
)


class ValidateIpv4TestCases(unittest.TestCase):
    def test_random(self):
        for i3923418 in range(720):
            x31241euq24 = bool(randint(0, 1))
            test = choice(test_tuple[x31241euq24])
            self.assertEqual(is_valid_ipv4(test), x31241euq24)


if __name__ == '__main__':
    unittest.main()
