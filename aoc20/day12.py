from collections import deque

import utils


def move_cardinal(direction, amount, x, y):
    if direction == "N":
        return (x, y + amount)
    if direction == "E":
        return (x + amount, y)
    if direction == "S":
        return (x, y - amount)
    if direction == "W":
        return (x - amount, y)


def rotate_ship(direction, amount, heading):
    steps = amount // 90
    dirs = deque(["N", "E", "S", "W"])
    dirs.rotate(-dirs.index(heading))
    dir_idx = steps % 4
    if direction == "L":
        return dirs[-dir_idx]
    if direction == "R":
        return dirs[dir_idx]


def rotate_waypoint(direction, amount, pos):
    steps = amount // 90
    steps = steps % 4
    if direction == "L":
        steps = -steps
    if steps == 0:
        return pos
    if steps in [1, -3]:
        return (pos[1], -pos[0])
    if steps % 2 == 0:
        return (-pos[0], -pos[1])
    if steps in [3, -1]:
        return (-pos[1], pos[0])


def execute_instruction_ship(instruction, x, y, heading):
    direction = instruction[0]
    amount = int(instruction[1:])
    if direction in ["N", "E", "S", "W"]:
        new_x, new_y = move_cardinal(direction, amount, x, y)
        return (new_x, new_y, heading)
    if direction in ["L", "R"]:
        new_heading = rotate_ship(direction, amount, heading)
        return (x, y, new_heading)
    if direction == "F":
        new_x, new_y = move_cardinal(heading, amount, x, y)
        return (new_x, new_y, heading)


def execute_instruction_waypoint(instruction, ship_pos, waypoint_pos):
    direction = instruction[0]
    amount = int(instruction[1:])
    if direction in ["N", "E", "S", "W"]:
        new_waypoint_pos = move_cardinal(direction,
                                         amount,
                                         waypoint_pos[0],
                                         waypoint_pos[1])
        return ship_pos, new_waypoint_pos
    if direction in ["L", "R"]:
        new_waypoint_pos = rotate_waypoint(direction, amount, waypoint_pos)
        return ship_pos, new_waypoint_pos
    if direction == "F":
        new_ship_pos = (ship_pos[0] + (amount * waypoint_pos[0]),
                        ship_pos[1] + (amount * waypoint_pos[1]))
        return new_ship_pos, waypoint_pos


def follow_instructions_ship(instructions, start_x, start_y, start_heading):
    x = start_x
    y = start_y
    heading = start_heading
    for instruction in instructions:
        x, y, heading = execute_instruction_ship(instruction, x, y, heading)
    return abs(x - start_x) + abs(y - start_y)


def follow_instructions_waypoint(instructions, ship_start, waypoint_start):
    ship_pos = ship_start
    waypoint_pos = waypoint_start
    for instruction in instructions:
        ship_pos, waypoint_pos = execute_instruction_waypoint(instruction,
                                                              ship_pos,
                                                              waypoint_pos)
    return abs(ship_pos[0] - ship_start[0]) + abs(ship_pos[1] - ship_start[1])


if __name__ == "__main__":
    input_instructions = utils.parse_file_lines("day12_input.txt", str)
    print("Part 1: {}".format(
        follow_instructions_ship(input_instructions, 0, 0, "E")))
    print("Part 2: {}".format(
        follow_instructions_waypoint(input_instructions, (0, 0), (10, 1))))
