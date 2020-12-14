import unittest

import day14
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        program = utils.parse_file_lines("day14_test_input1.txt", str)
        self.assertEqual(
            day14.initialize(program),
            165)

    def test_second(self):
        program = utils.parse_file_lines("day14_test_input2.txt", str)
        self.assertEqual(
            day14.initialize_2(program),
            208)
