import unittest

import day12
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        instructions = utils.parse_file_lines("day12_test_input1.txt", str)
        self.assertEqual(
            day12.follow_instructions_ship(instructions, 0, 0, "E"),
            25)

    def test_second(self):
        instructions = utils.parse_file_lines("day12_test_input1.txt", str)
        self.assertEqual(
            day12.follow_instructions_waypoint(instructions,
                                               (0, 0),
                                               (10, 1)),
            286)
