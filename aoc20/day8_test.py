import unittest

import day8
import utils


class TestDay7(unittest.TestCase):
    def test_first(self):
        program = utils.parse_file_lines("day8_test_input1.txt", str)
        program = [line.strip() for line in program]
        self.assertEqual(day8.execute_code(program)[0], 5)

    def test_second(self):
        program = utils.parse_file_lines("day8_test_input1.txt", str)
        program = [line.strip() for line in program]
        self.assertEqual(day8.change_code(program), 8)
