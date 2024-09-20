import unittest
from datetime import datetime
from pacote_utilitarios import get_current_date, format_date, parse_date, days_between, add_days_to_date, is_weekend, is_weekday, get_first_day_of_month, get_last_day_of_month

class TestDateUtils(unittest.TestCase):

    def test_format_date(self):
        self.assertEqual(format_date(get_current_date()))   
    def test_parse_date(self):
        self.assertEqual(parse_date("2024-01-01"), get_current_date())    
    def test_days_between(self):
        self.assertEqual(days_between(parse_date("2024-01-01"), get_current_date()))    
    def test_add_days_to_date(self):
        self.assertEqual(add_days_to_date(get_current_date(), 10))    
    def test_is_weekend(self):
        self.assertEqual(is_weekend(get_current_date()))    
    def test_is_weekday(self):
        self.assertEqual(is_weekday(get_current_date()))    
    def test_get_first_day_of_month(self):
        self.assertEqual(get_first_day_of_month(get_current_date()))    
    def test_get_last_day_of_month(date):
        self.assertEqual(get_last_day_of_month(get_current_date()))    

if __name__ == '__main__':
    unittest.main()