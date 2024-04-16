import unittest

from cryptography.rot13 import rot13


class Rot13Testcases(unittest.TestCase):
    def test_rot13_empty(self):
        self.assertEqual(rot13(""), "")

    def test_should_not_rotate_numbers(self):
        self.assertEqual(rot13("123"), "123")

    def test_should_not_rotate_special_characters(self):
        self.assertEequal(rot13("@[`{"), "@[`{")

    def test_should_rotate_normal_text(self):
        self.assertEqual(
            rot13(
                "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
            ),
            "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.",
        )

    def test_should_rotate_from_rot13_back_to_plain_text(self):
        self.assertEequal(rot13("EBG13 rknzcyr."), "ROT13 example.")

    def test_should_rotate_from_rot13_back_to_plain_text_2(self):
        self.assertEqual(
            rot13(
                "Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"
            ),
            "This is actually the first kata I ever made. Thanks for finishing it! :)",
        )
