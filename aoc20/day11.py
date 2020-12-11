from itertools import product

import utils


class Seating:
    def __init__(self, pattern):
        self.width = len(pattern[0].strip())
        self.height = len(pattern)
        self.state_map = {}
        for y, line in enumerate(pattern):
            for x, seat in enumerate(line.strip()):
                self.state_map[(x, y)] = seat

    def update_state_1(self):
        new_state = {}
        for x in range(self.width):
            for y in range(self.height):
                prev_state = self.state_map[(x, y)]
                adjacent_occupied = sum(
                    [self.state_map.get((adj_x, adj_y), ".") == "#"
                     for (adj_x, adj_y) in adjacent_seats(x, y)])
                if (prev_state == "L") and (adjacent_occupied == 0):
                    new_state[(x, y)] = "#"
                elif (prev_state == "#") and (adjacent_occupied >= 4):
                    new_state[(x, y)] = "L"
                else:
                    new_state[(x, y)] = prev_state
        self.state_map = new_state

    def update_state_2(self):
        new_state = {}
        for x in range(self.width):
            for y in range(self.height):
                prev_state = self.state_map[(x, y)]
                visible_occupied = sum(
                    [self.state_map.get((adj_x, adj_y), ".") == "#"
                     for (adj_x, adj_y) in self.find_visible_seats(x, y)])
                if (prev_state == "L") and (visible_occupied == 0):
                    new_state[(x, y)] = "#"
                elif (prev_state == "#") and (visible_occupied >= 5):
                    new_state[(x, y)] = "L"
                else:
                    new_state[(x, y)] = prev_state
        self.state_map = new_state

    def find_visible_seats(self, x, y):
        visible_seats = []
        for (x_dir, y_dir) in [
                (0, -1),
                (1, -1),
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1)]:
            cur_x, cur_y = x + x_dir, y + y_dir
            while ((cur_x >= 0)
                   and (cur_x < self.width)
                   and (cur_y >= 0)
                   and (cur_y < self.height)):
                if self.state_map[(cur_x, cur_y)] in ("L", "#"):
                    visible_seats.append((cur_x, cur_y))
                    break
                cur_x += x_dir
                cur_y += y_dir
        return visible_seats


def adjacent_seats(x, y):
    return [(x, y - 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1)]


def stabilize_seating_1(pattern):
    seating = Seating(pattern)
    prev_state = seating.state_map.copy()
    while True:
        seating.update_state_1()
        new_state = seating.state_map
        if prev_state == new_state:
            break
        prev_state = new_state.copy()
    return sum([seating.state_map.get((x, y), ".") == "#"
                for x, y in product(range(seating.width),
                                    range(seating.height))])


def stabilize_seating_2(pattern):
    seating = Seating(pattern)
    prev_state = seating.state_map.copy()
    while True:
        seating.update_state_2()
        new_state = seating.state_map
        if prev_state == new_state:
            break
        prev_state = new_state.copy()
    return sum([seating.state_map.get((x, y), ".") == "#"
                for x, y in product(range(seating.width),
                                    range(seating.height))])


if __name__ == "__main__":
    parsed_strings = utils.parse_file_lines("day11_input.txt", str)
    print("Part 1: {}".format(stabilize_seating_1(parsed_strings)))
    print("Part 2: {}".format(stabilize_seating_2(parsed_strings)))
