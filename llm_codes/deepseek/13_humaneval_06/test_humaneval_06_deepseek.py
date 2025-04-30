import unittest
from humaneval_06_deepseek import parse_nested_parens


class TestParseNestedParens(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
    
    def test_single_group(self):
        self.assertEqual(parse_nested_parens('(())'), [2])
        self.assertEqual(parse_nested_parens('()'), [1])
        self.assertEqual(parse_nested_parens('((()))'), [3])
    
    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('() () ()'), [1, 1, 1])
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
    
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])
    
    def test_no_parentheses(self):
        self.assertEqual(parse_nested_parens('abc def'), [])
    
    def test_mixed_characters(self):
        self.assertEqual(parse_nested_parens('(a(b)c) (d(e(f)g)h)'), [2, 3])
    
    def test_unbalanced_parentheses(self):
        with self.assertRaises(IndexError):
            parse_nested_parens('(()')
        with self.assertRaises(IndexError):
            parse_nested_parens('())')

if __name__ == '__main__':
    unittest.main()
