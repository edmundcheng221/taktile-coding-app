import unittest
from app import *


class TestFold(unittest.TestCase):

    def test_fold_right(self):
        # Add
        self.assertEqual(Fold.fold_right(add, [1, 2, 3, 4, 5]), 15)
        self.assertEqual(Fold.fold_right(add, [2, 4, 6], 0), 12)
        self.assertEqual(Fold.fold_right(add, []), 0)
        # # Subtract
        self.assertEqual(Fold.fold_right(subtract, [1, 2, 3, 4, 5]), 3)
        self.assertEqual(Fold.fold_right(subtract, [2, 4, 6], 0), 4)
        self.assertEqual(Fold.fold_right(subtract, []), 0)
        # # Multiply
        self.assertEqual(Fold.fold_right(multiply, [1, 2, 3, 4, 5]), 120)
        self.assertEqual(Fold.fold_right(multiply, [2, 4, 6], 0), 0)
        self.assertEqual(Fold.fold_right(multiply, []), 0)
        # Divide
        self.assertEqual(Fold.fold_right(divide, [1, 2, 3, 4, 5]), 1/(2/(3/(4/5))))
        self.assertEqual(Fold.fold_right(divide, [2, 4, 8]), 4)
        self.assertEqual(Fold.fold_right(divide, [2, 4, 8], 0), None)

    def test_fold_left(self):
        # Add
        self.assertEqual(Fold.fold_left(add, [1, 2, 3, 4, 5]), 15)
        self.assertEqual(Fold.fold_left(add, [2, 4, 6], 0), 12)
        self.assertEqual(Fold.fold_left(add, []), 0)
        # Subtract
        self.assertEqual(Fold.fold_left(subtract, [1, 2, 3, 4, 5]), -13)
        self.assertEqual(Fold.fold_left(subtract, [2, 4, 6], 0), -12)
        self.assertEqual(Fold.fold_left(subtract, [], 0), 0)
        # Multiply
        self.assertEqual(Fold.fold_left(multiply, [1, 2, 3, 4, 5]), 120)
        self.assertEqual(Fold.fold_left(multiply, [2, 4, 6], 0), 0)
        self.assertEqual(Fold.fold_left(multiply, [], 0), 0)
        # Divide
        self.assertEqual(Fold.fold_left(divide, [1, 2, 3, 4, 5]), (((1/2)/3)/4)/5)
        self.assertEqual(Fold.fold_left(divide, [2, 4, 8]) , 0.0625)
        self.assertEqual(Fold.fold_left(divide, [2, 4, 8], 0) , 0)


if __name__ == "__main__":
    unittest.main()
