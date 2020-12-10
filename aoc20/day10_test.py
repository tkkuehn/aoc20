import unittest

import day10
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        nums = utils.parse_file_lines("day10_test_input1.txt", int)
        self.assertEqual(day10.construct_chain(nums), 35)
        nums = utils.parse_file_lines("day10_test_input2.txt", int)
        self.assertEqual(day10.construct_chain(nums), 220)

    def test_second(self):
        nums = utils.parse_file_lines("day10_test_input1.txt", int)
        self.assertEqual(day10.find_chains(nums), 8)
        nums = utils.parse_file_lines("day10_test_input2.txt", int)
        self.assertEqual(day10.find_chains(nums), 19208)
