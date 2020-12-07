import unittest

import day7
import utils


class TestDay7(unittest.TestCase):
    def test_first(self):
        spec = utils.parse_file_lines("day7_test_input1.txt", str)
        relationship_map = day7.parse_all_lines(spec)
        gold_parents = set()
        day7.find_parents(relationship_map, "shiny gold", gold_parents)
        self.assertEqual(
            gold_parents,
            {"bright white", "muted yellow", "dark orange", "light red"})

    def test_second(self):
        spec = utils.parse_file_lines("day7_test_input1.txt", str)
        relationship_map = day7.parse_all_lines(spec)
        self.assertEqual(day7.count_bags(relationship_map, "shiny gold"), 32)
