import unittest

import day1

class TestDay1(unittest.TestCase):
    def test_first(self):
        with open("test_day1_1.txt") as f:
            nums = [int(line) for line in f]
        self.assertEqual(day1.find_sum_2(nums, 2020), 514579)

    def test_second(self):
        with open("test_day1_1.txt") as f:
            nums = [int(line) for line in f]
        self.assertEqual(day1.find_sum_3(nums, 2020), 241861950)
