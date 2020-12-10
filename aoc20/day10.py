from collections import Counter

import utils


def find_chains(joltages):
    joltages = sorted(joltages + [0, max(joltages) + 3])
    joltage_set = set(joltages)
    joltage_map = {}
    for joltage in joltages:
        inputs = set([joltage - 1, joltage - 2, joltage - 3]) & joltage_set
        if len(inputs) > 0:
            joltage_map[joltage] = sum(
                [joltage_map[input] for input in inputs])
        else:
            joltage_map[joltage] = 1
    return joltage_map[max(joltages)]


def construct_chain(joltages):
    diff_counts = Counter()
    joltages = sorted(joltages + [0])
    for idx, joltage in enumerate(joltages):
        if idx == len(joltages) - 1:
            difference = 3
        else:
            difference = joltages[idx + 1] - joltage
        diff_counts[difference] += 1
    return diff_counts[1] * diff_counts[3]


if __name__ == "__main__":
    input_nums = utils.parse_file_lines("day10_input.txt", int)
    print("Part 1: {}".format(construct_chain(input_nums)))
    print("Part 2: {}".format(find_chains(input_nums)))
