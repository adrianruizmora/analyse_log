import unittest
import functions.functions as f

from collections import OrderedDict

class TestFunctions(unittest.TestCase):
    """
    Class that test all functions from the functions module
    """

    def test_time_diff(self):
        """
        Method tests the time difference,
        given two times on the format hh:mm.
        """
        time1 = ("09:20", "11:00") # normal time
        time2 = ("11:00", "09:20") # negatif time
        time3 = ("00:00", "00:00") # nul time
        self.assertEqual(f.time_diff(time1[0], time1[1]), 100)
        self.assertEqual(f.time_diff(time2[0], time2[1]), -1)
        self.assertEqual(f.time_diff(time3[0], time3[1]), 0)

    def test_percentage(self):
        """
        Method that tests the percentage of a task in
        a dictionnary given its value. 
        """
        tasks1 = {"accompagner": 30, "break": 50, "manger": 25} # normal percentage
        tasks2 = {"break": 0} # nul percentage
        tasks3 = {"activity": -1} # negatif percentage
        self.assertEqual(f.percentage(tasks1, "accompagner"), 28)
        self.assertEqual(f.percentage(tasks2, "break"), 0)
        self.assertEqual(f.percentage(tasks3, "activity"), 0)

    def test_read_file(self):
        ## diff
        expected_output = open("expected_output.txt")
        output = open("output.txt")
        self.assertListEqual(
            list(expected_output),
            list(output)
        )
        expected_output.close()
        output.close()

    def test_write_file(self):
        pass


if __name__ == "__main__":
    unittest.main()
