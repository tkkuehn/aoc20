import unittest

import day16
import utils


class TestDay1(unittest.TestCase):
    def test_first(self):
        input_spec = "".join(
            utils.parse_file_lines("day16_test_input1.txt", str))
        self.assertEqual(day16.find_error_rate(input_spec), 71)
