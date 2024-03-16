import unittest
from exercise_1 import replace_last

class TestReplaceLast(unittest.TestCase):
    def test_replace_last(self):
        # Test when the list has more than one element
        self.assertEqual(replace_last([2, 3, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(replace_last([1, 2, 3, 4]), [4, 1, 2, 3])

        # Test when the list has only one element
        self.assertEqual(replace_last([1]), [1])

        # Test when the list is empty
        self.assertEqual(replace_last([]), [])

if __name__ == '__main__':
    unittest.main()
