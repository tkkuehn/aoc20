import unittest

import day2, utils

class TestDay1(unittest.TestCase):
    def test_first(self):
        passwords = utils.parse_file_lines("day2_test_input1.txt", str)
        self.assertEqual(day2.find_valid_passwords(passwords), 2)

    def test_second(self):
        passwords = utils.parse_file_lines("day2_test_input1.txt", str)
        self.assertEqual(day2.find_valid_passwords_2(passwords), 1)
