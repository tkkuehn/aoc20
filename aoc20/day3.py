from math import prod

import utils


class Hill:
    def __init__(self, input_pattern):
        self.pattern_width = len(input_pattern[0]) - 1
        self.height = len(input_pattern)
        self.tree_locs = set()
        for y, line in enumerate(input_pattern):
            self._find_trees(line, y)

    def _find_trees(self, line, y):
        for x, content in enumerate(line):
            if content == "#":
                self.tree_locs.add((x, y))

    def check_angle(self, x_increment, y_increment):
        current_x, current_y = (0, 0)
        num_trees = 0
        while current_y < self.height:
            current_x = (current_x + x_increment) % self.pattern_width
            current_y += y_increment
            if (current_x, current_y) in self.tree_locs:
                num_trees += 1
        return num_trees


if __name__ == "__main__":
    parsed_strings = utils.parse_file_lines("day3_input.txt", str)
    hill = Hill(parsed_strings)
    print("Part 1: {}".format(hill.check_angle(3, 1)))
    part_2_answer = prod([hill.check_angle(1, 1),
                          hill.check_angle(3, 1),
                          hill.check_angle(5, 1),
                          hill.check_angle(7, 1),
                          hill.check_angle(1, 2)])
    print("Part 2: {}".format(part_2_answer))
