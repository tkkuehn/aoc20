import unittest

import day15
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        for num_str, expected in zip(
                utils.parse_file_lines("day15_test_input1.txt", str),
                [436, 1, 10, 27, 78, 438, 1836]):
            self.assertEqual(
                day15.play_game(num_str, 2020),
                expected)

    def test_second(self):
        for num_str, expected in zip(
                utils.parse_file_lines("day15_test_input1.txt", str),
                [175594, 2578, 3544142, 261214, 6895259, 18, 362]):
            self.assertEqual(
                day15.play_game(num_str, 30000000),
                expected)
