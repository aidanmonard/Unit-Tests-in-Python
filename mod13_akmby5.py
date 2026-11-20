
import unittest
from datetime import datetime


class TestStockInputs(unittest.TestCase):

    
    def test_symbol(self):
        self.assertRegex("AAPL", r"^[A-Z]{1,7}$")
        self.assertRegex("MSFT", r"^[A-Z]{1,7}$")
        self.assertNotRegex("apple", r"^[A-Z]{1,7}$")
        self.assertNotRegex("ABCDEFGH", r"^[A-Z]{1,7}$")
        self.assertNotRegex("AAP1", r"^[A-Z]{1,7}$")

 
    def test_chart_type(self):
        self.assertIn("1", ["1", "2"])
        self.assertIn("2", ["1", "2"])
        self.assertNotIn("3", ["1", "2"])
        self.assertNotIn("12", ["1", "2"])

 
    def test_time_series(self):
        for value in ["1", "2", "3", "4"]:
            self.assertIn(value, ["1", "2", "3", "4"])

        self.assertNotIn("5", ["1", "2", "3", "4"])
        self.assertNotIn("12", ["1", "2", "3", "4"])

    
    def test_start_date(self):
        self.assertTrue(self.valid_date("2026-01-15"))
        self.assertTrue(self.valid_date("2025-12-31"))
        self.assertFalse(self.valid_date("01-15-2026"))
        self.assertFalse(self.valid_date("2026-13-15"))
        self.assertFalse(self.valid_date("2026-02-30"))

    
    def test_end_date(self):
        self.assertTrue(self.valid_date("2026-11-19"))
        self.assertTrue(self.valid_date("2025-06-10"))
        self.assertFalse(self.valid_date("11-19-2026"))
        self.assertFalse(self.valid_date("2026-14-19"))
        self.assertFalse(self.valid_date("2026-02-30"))

    def valid_date(self, date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    unittest.main()
