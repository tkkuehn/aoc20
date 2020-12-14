from itertools import count

import utils


def find_earliest_bus(notes):
    earliest = int(notes[0])
    buses = notes[1].strip().split(",")
    buses = [int(bus) for bus in buses if bus != "x"]
    wait_times = {bus: (bus - (earliest % bus)) % bus for bus in buses}
    shortest_wait = min(wait_times.items(), key=lambda x: x[1])
    return shortest_wait[0] * shortest_wait[1]


def find_bus_pattern(notes):
    buses = notes[1].strip().split(",")
    max_bus = max([int(bus) for bus in buses if bus != "x"])
    max_idx = buses.index(str(max_bus))
    num_conditions = sum([bus != "x" for bus in buses])
    for candidate in count(max_bus, max_bus):
        candidate -= max_idx
        if (sum([(int(bus) - (candidate % int(bus))) % int(bus) == idx
                 for idx, bus in enumerate(buses) if bus != "x"])
                == num_conditions):
            return candidate


if __name__ == "__main__":
    input_notes = utils.parse_file_lines("day13_input.txt", str)
    print("Part 1: {}".format(find_earliest_bus(input_notes)))
    print("Part 2: {}".format(find_bus_pattern(input_notes)))
