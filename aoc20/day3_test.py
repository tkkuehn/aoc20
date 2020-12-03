import unittest

import day3, utils

class TestDay1(unittest.TestCase):
    def test_first(self):
        input_pattern = utils.parse_file_lines("day3_test_input1.txt", str)
        hill = day3.Hill(input_pattern)
        self.assertEqual(hill.check_angle(3, 1), 7)

    def test_second(self):
        input_pattern = utils.parse_file_lines("day3_test_input1.txt", str)
        hill = day3.Hill(input_pattern)
        for x, y, ans in zip([1, 3, 5, 7, 1],
                             [1, 1, 1, 1, 2],
                             [2, 7, 3, 4, 2]):
            self.assertEqual(hill.check_angle(x, y), ans)
