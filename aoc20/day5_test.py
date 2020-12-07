import unittest

import day5
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        seat_input = utils.parse_file_lines("day5_test_input1.txt", str)
        for seat, seat_id in zip(seat_input, [357, 567, 119, 820]):
            self.assertEqual(day5.find_id(seat), seat_id)
