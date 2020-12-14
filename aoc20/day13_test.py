import unittest

import day13
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        notes = utils.parse_file_lines("day13_test_input1.txt", str)
        self.assertEqual(
            day13.find_earliest_bus(notes),
            295)

    def test_second(self):
        notes = utils.parse_file_lines("day13_test_input1.txt", str)
        self.assertEqual(
            day13.find_bus_pattern(notes),
            1068781)
