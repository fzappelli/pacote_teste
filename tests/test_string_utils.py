import unittest
from pacote_utilitarios import to_upper, capitalize_first_letter, strip_spaces, is_palindrome, count_occurrences, replace_substring, reverse_string

class TestStringUtils(unittest.TestCase):
    
    def test_to_upper(self):
        to_upper("hello"), "HELLO")
    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter("  Hello World!  "))
    def test_strip_spaces(self):
        self.assertEqual(strip_spaces("  Hello World!  "))
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("A man a plan a canal Panama"))
    def test_count_occurrences(self):    
        self.assertEqual(count_occurrences("banana", "na"))
    def test_replace_substring(self):   
        self.assertEqual(replace_substring("hello world", "world", "there"))
    def test_reverse_string(self):    
        self.assertEqual(reverse_string("hello"))


if __name__ == '__main__':
    unittest.main()