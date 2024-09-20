import unittest
from pacote_utilitarios import remove_duplicates, flatten_list, find_max, find_min, chunk_list, sort_list, filter_even_numbers, filter_odd_numbers, get_unique_elements

class TestListUtils(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4], [5, 6]]))
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 2, 3, 4, 4, 5]))
    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 2, 3, 4, 4, 5]))
    def test_chunk_list(self):
        self.assertEqual(chunk_list([1, 2, 2, 3, 4, 4, 5], 2))
    def test_sort_list(self):
        self.assertEqual(sort_list([1, 2, 2, 3, 4, 4, 5]))
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 2, 3, 4, 4, 5]))
    def test_filter_odd_numbers(self):
        self.assertEqual(filter_odd_numbers([1, 2, 2, 3, 4, 4, 5]))
    def test_get_unique_elements(self):
        self.assertEqual(get_unique_elements([1, 2, 2, 3, 4, 4, 5]))

if __name__ == '__main__':
    unittest.main()