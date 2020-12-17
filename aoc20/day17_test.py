import unittest

import day17
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        input_pattern = utils.parse_file_lines("day17_test_input1.txt", str)
        self.assertEqual(day17.sim_six_cycles_3d(input_pattern), 112)

    def test_second(self):
        input_pattern = utils.parse_file_lines("day17_test_input1.txt", str)
        self.assertEqual(day17.sim_six_cycles_4d(input_pattern), 848)
