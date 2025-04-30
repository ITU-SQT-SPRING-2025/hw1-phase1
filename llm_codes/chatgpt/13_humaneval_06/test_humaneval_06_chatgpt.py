import unittest
from humaneval_06_chatgpt import parse_nested_parens


class TestParseNestedParens(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('()'), [1])
        self.assertEqual(parse_nested_parens('(())'), [2])
        self.assertEqual(parse_nested_parens('(((())))'), [4])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('() ()'), [1, 1])
        self.assertEqual(parse_nested_parens('((())) (()) ()'), [3, 2, 1])

    def test_empty_input(self):
        self.assertEqual(parse_nested_parens(''), [])
        self.assertEqual(parse_nested_parens('   '), [])

    def test_complex_nesting(self):
        self.assertEqual(parse_nested_parens('(()(())) ((()())())'), [3, 3])

    def test_unbalanced_but_still_counted(self):
        # Our function assumes input is correct, but even if not, it just tracks max depth
        self.assertEqual(parse_nested_parens('((()'), [3])
        self.assertEqual(parse_nested_parens('(()))'), [2])

if __name__ == "__main__":
    unittest.main()
