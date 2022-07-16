import unittest
from main.main import *


class TestDate(unittest.TestCase):
    def test_list(self):
        self.assertEqual(compare_date("16.07.2022 00:00", 0), "The first date has been reached! (16.07.2022 00:00)")
        self.assertEqual(compare_date("18.07.2022 00:00", 1), "The second date will be reached! (18.07.2022 00:00)")
        self.assertEqual(compare_date("15.07.2022 00:00", 2), "The third has been reached! (15.07.2022 00:00)")
        self.assertEqual(compare_date("14.07.2022 00:00", 3), "The fourth has been reached! (14.07.2022 00:00)")
        self.assertEqual(compare_date("17.07.2022 00:00", 4), "The fifth date date current date! (17.07.2022 00:00)")
        self.assertEqual(compare_date("16.07.2022 00:00", 5), "The sixth date has been reached! (16.07.2022 00:00)")
        self.assertEqual(compare_date("16.07.2022 00:00", 6), "The seventh date has been reached! (16.07.2022 00:00)")
        self.assertEqual(compare_date("16.07.2022 00:00", 7), "The eighth date has been reached! (16.07.2022 00:00)")


if __name__ == "__main__":
    unittest.main()
