import unittest

import day11
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        input_pattern = utils.parse_file_lines("day11_test_input1.txt", str)
        self.assertEqual(day11.stabilize_seating_1(input_pattern), 37)

    def test_second(self):
        input_pattern = utils.parse_file_lines("day11_test_input1.txt", str)
        self.assertEqual(day11.stabilize_seating_2(input_pattern), 26)
