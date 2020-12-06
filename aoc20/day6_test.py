import unittest

import day6
import utils

class TestDay1(unittest.TestCase):
    def test_first(self):
        groups = utils.parse_file_groups("day6_test_input1.txt")
        self.assertEqual(sum(day6.find_all_answers(groups)), 11)

    def test_second(self):
        groups = utils.parse_file_groups("day6_test_input1.txt")
        self.assertEqual(sum(day6.find_all_common_answers(groups)), 6)

