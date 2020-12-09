import unittest

import day9
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        nums = utils.parse_file_lines("day9_test_input1.txt", int)
        self.assertEqual(day9.find_invalid_number(nums, 5), 127)

    def test_second(self):
        nums = utils.parse_file_lines("day9_test_input1.txt", int)
        self.assertEqual(day9.find_range_sum(nums, 127), 62)
