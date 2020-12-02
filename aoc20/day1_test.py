import unittest

import day1, utils

class TestDay1(unittest.TestCase):
    def test_first(self):
        nums = utils.parse_file_lines("day1_test_input1.txt", int)
        self.assertEqual(day1.find_sum_2(nums, 2020), 514579)

    def test_second(self):
        nums = utils.parse_file_lines("day1_test_input1.txt", int)
        self.assertEqual(day1.find_sum_3(nums, 2020), 241861950)
