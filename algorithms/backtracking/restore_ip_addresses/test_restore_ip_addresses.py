import unittest

from . import restore_ip_addresses


class RestoreIpAddressesTestCase(unittest.TestCase):
    def test_25525511135(self):
        """should return ["255.255.11.135","255.255.111.35"] from 25525511135"""
        s = "25525511135"
        expected = ["255.255.11.135", "255.255.111.35"]
        actual = restore_ip_addresses(s)
        self.assertEqual(expected, actual)

    def test_0000(self):
        """should return ["0.0.0.0"] from 0000"""
        s = "0000"
        expected = ["0.0.0.0"]
        actual = restore_ip_addresses(s)
        self.assertEqual(expected, actual)

    def test_101023(self):
        """should return ["0.0.0.0"] from 101023"""
        s = "101023"
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        actual = restore_ip_addresses(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
