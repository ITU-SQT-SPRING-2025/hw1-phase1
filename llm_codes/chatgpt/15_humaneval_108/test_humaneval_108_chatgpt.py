import unittest

from humaneval_108_chatgpt import count_nums

class TestCountNums(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(count_nums([]), 0)

    def test_single_negative_number(self):
        self.assertEqual(count_nums([-1]), 0)

    def test_mixed_sign_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_all_positive(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

    def test_all_zeroes(self):
        self.assertEqual(count_nums([0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(count_nums([1234, -5678, 0, 9999]), 3)

    def test_only_negatives(self):
        self.assertEqual(count_nums([-1, -2, -3]), 0)

    def test_mixed_complex(self):
        self.assertEqual(count_nums([-12, -34, 56, -78, 90]), 2)

if __name__ == "__main__":
    unittest.main()
