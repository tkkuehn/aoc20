import unittest

import day4
import utils

class TestDay1(unittest.TestCase):
    def test_first(self):
        batch = "".join(utils.parse_file_lines("day4_test_input1.txt", str)) + "\n"
        self.assertEqual(day4.find_valid_passports(batch), 2)

    def test_second(self):
        batch2 = "".join(utils.parse_file_lines("day4_test_input2.txt", str)) + "\n"
        self.assertEqual(day4.find_valid_passports_2(batch2), 0)
        batch3 = "".join(utils.parse_file_lines("day4_test_input3.txt", str)) + "\n"
        self.assertEqual(day4.find_valid_passports_2(batch3), 4)
