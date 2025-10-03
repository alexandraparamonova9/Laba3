import unittest
from main import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    def test_height_one(self):
        tree = gen_bin_tree(1, 14)
        expected = {"value": 14, "left": None, "right": None}
        self.assertEqual(tree, expected)

    def test_height_two(self):
        tree = gen_bin_tree(2, 14)
        expected = {
            "value": 14,
            "left": {"value": -11, "left": None, "right": None},
            "right": {"value": 28, "left": None, "right": None},
        }
        self.assertEqual(tree, expected)

    def test_height_zero(self):
        tree = gen_bin_tree(0, 14)
        self.assertIsNone(tree)

    def test_height_three(self):
        tree = gen_bin_tree(3, 2)
        self.assertIsInstance(tree, dict)
        self.assertEqual(tree["value"], 2)
        self.assertIn("left", tree)
        self.assertIn("right", tree)


if __name__ == "__main__":
    unittest.main()
