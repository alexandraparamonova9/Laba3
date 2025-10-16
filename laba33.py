from laba3 import binary_tree
import unittest
from typing import Dict, List


class TestBinaryTree(unittest.TestCase):

    def test_height_0(self):
        result = binary_tree(0, 5, left_leaf=lambda x: x + 1, right_leaf=lambda x: x ** 2)
        expected = {"5": []}
        self.assertEqual(result, expected)

    def test_height_1(self):
        result = binary_tree(1, 5, left_leaf=lambda x: x + 1, right_leaf=lambda x: x ** 2)
        expected = {"5": [{"6": []}, {"25": []}]}
        self.assertEqual(result, expected)

    def test_height_2(self):
        result = binary_tree(2, 5, left_leaf=lambda x: x + 1, right_leaf=lambda x: x ** 2)
        expected = {
            "5": [
                {"6": [{"7": []}, {"36": []}]},
                {"25": [{"26": []}, {"625": []}]}
            ]
        }
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
