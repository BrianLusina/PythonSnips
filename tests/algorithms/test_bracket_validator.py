import unittest

from algorithms.bracket_validator import check_brackets_3, check_brackets_1, check_brackets_2


class BracketsTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(True, check_brackets_1('((()))'))

    def test2(self):
        self.assertEqual(True, check_brackets_1('(()())'))

    def test3(self):
        self.assertEqual(False, check_brackets_1('((()'))

    def test4(self):
        self.assertEqual(False, check_brackets_1('())('))

    def test_input_empty(self):
        self.assertEqual(check_brackets_1(""), True)

    def test_single(self):
        self.assertEqual(check_brackets_1("{}"), True)

    def test_unclosed(self):
        self.assertEqual(check_brackets_1("{{"), False)

    def test_wrong_order(self):
        self.assertEqual(check_brackets_1("}{"), False)

    def test_mixed_not_nested(self):
        self.assertEqual(check_brackets_1("{}[]"), True)

    def test_mixed_nested(self):
        self.assertEqual(check_brackets_1("{[]}"), True)

    def test_improperly_nested(self):
        self.assertEqual(check_brackets_1("{[}]"), False)

    def test_not_opened_nested(self):
        self.assertEqual(check_brackets_1("{[)][]}"), False)

    def test_nested_ensemble(self):
        self.assertEqual(check_brackets_1("{[]([()])}"), True)

    def test_input_empty_2(self):
        self.assertEqual(check_brackets_2(""), True)

    def test_single_2(self):
        self.assertEqual(check_brackets_2("{}"), True)

    def test_unclosed_2(self):
        self.assertEqual(check_brackets_2("{{"), False)

    def test_wrong_order_2(self):
        self.assertEqual(check_brackets_2("}{"), False)

    def test_mixed_not_nested_2(self):
        self.assertEqual(check_brackets_2("{}[]"), True)

    def test_mixed_nested_2(self):
        self.assertEqual(check_brackets_2("{[]}"), True)

    def test_improperly_nested_2(self):
        self.assertEqual(check_brackets_2("{[}]"), False)

    def test_not_opened_nested_2(self):
        self.assertEqual(check_brackets_2("{[)][]}"), False)

    def test_nested_ensemble_2(self):
        self.assertEqual(check_brackets_2("{[]([()])}"), True)

    def test_input_empty_3(self):
        self.assertEqual(check_brackets_3(""), True)

    def test_single_3(self):
        self.assertEqual(check_brackets_3("{}"), True)

    def test_unclosed_3(self):
        self.assertEqual(check_brackets_3("{{"), False)

    def test_wrong_order_3(self):
        self.assertEqual(check_brackets_3("}{"), False)

    def test_mixed_not_nested_3(self):
        self.assertEqual(check_brackets_3("{}[]"), True)

    def test_mixed_nested_3(self):
        self.assertEqual(check_brackets_3("{[]}"), True)

    def test_improperly_nested_3(self):
        self.assertEqual(check_brackets_3("{[}]"), False)

    def test_not_opened_nested_3(self):
        self.assertEqual(check_brackets_3("{[)][]}"), False)

    def test_nested_ensemble_3(self):
        self.assertEqual(check_brackets_3("{[]([()])}"), True)


if __name__ == '__main__':
    unittest.main()
