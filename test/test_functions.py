import unittest
import functions.functions as f

from collections import OrderedDict

class TestFonctions(unittest.TestCase):
    """
    Class that test all functions from the functions module
    """

    def setUp(self):
        """
        Setup variables that are going to be used by the methods
        """
        self.time1 = "09:20"
        self.time2 = "11:00"
        self.tasks = {"accompagner": 30, "break": 50, "manger": 25}

    def test_time_diff(self):
        self.assertIsInstance(f.time_diff(self.time1, self.time2), int)
        self.assertEqual(f.time_diff(self.time1, self.time2), 100)

    def test_percentage(self):
        self.assertEqual(f.percentage(self.tasks, "accompagner"), 28)

    def test_read_file(self):
        self.assertIsInstance(f.read_file("planning.log"), OrderedDict)

    def test_write_file(self):
        pass


if __name__ == "__main__":
    unittest.main()