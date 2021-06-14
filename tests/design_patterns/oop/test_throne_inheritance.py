import unittest

from design_patterns.oop.throne_inheritance import ThroneInheritance


class ThroneInheritanceTestCase(unittest.TestCase):
    def test_order_with_one_child(self):
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        self.assertEqual(["king", "andy"], t.get_inheritance_order())

    def test_order_with_two_children(self):
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        t.birth("king", "bob")
        self.assertEqual(["king", "andy", "bob"], t.get_inheritance_order())

    def test_order_with_three_children(self):
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        t.birth("king", "bob")
        t.birth("king", "catherine")
        self.assertEqual(["king", "andy", "bob", "catherine"], t.get_inheritance_order())

    def test_order_with_grand_children_one(self):
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        t.birth("king", "bob")
        t.birth("king", "catherine")
        t.birth("andy", "mathew")
        self.assertEqual(["king", "andy", "mathew", "bob", "catherine"], t.get_inheritance_order())

    def test_order_with_grand_children_two(self):
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        t.birth("king", "bob")
        t.birth("king", "catherine")
        t.birth("andy", "mathew")
        t.birth("bob", "alex")
        t.birth("bob", "asha")
        self.assertEqual(["king", "andy", "mathew", "bob", "alex", "asha", "catherine"], t.get_inheritance_order())

    def test_order_with_one_death(self):
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        t.birth("king", "bob")
        t.birth("king", "catherine")
        t.birth("andy", "mathew")
        t.birth("bob", "alex")
        t.birth("bob", "asha")
        t.death("bob")
        self.assertEqual(["king", "andy", "mathew", "alex", "asha", "catherine"], t.get_inheritance_order())


if __name__ == '__main__':
    unittest.main()
