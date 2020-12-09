from collections import deque

import utils


def find_invalid_number(sequence, len_preamble):
    current = deque(sequence[:len_preamble], len_preamble)
    for new_num in sequence[len_preamble:]:
        existing = set(current)
        found_pair = False
        for element in current:
            if new_num - element in existing - set([element]):
                found_pair = True
        if not found_pair:
            return new_num
        current.append(new_num)
    raise ValueError("All numbers valid")


def find_range_sum(sequence, target):
    for start_idx, _ in enumerate(sequence):
        for end_idx in range(start_idx + 2, len(sequence) + 1):
            contiguous = sequence[start_idx:end_idx]
            range_sum = sum(contiguous)
            if range_sum == target:
                return min(contiguous) + max(contiguous)
            elif range_sum > target:
                continue
    raise ValueError("No valid range")


if __name__ == "__main__":
    input_nums = utils.parse_file_lines("day9_input.txt", int)
    invalid_number = find_invalid_number(input_nums, 25)
    print("Part 1: {}".format(invalid_number))
    print("Part 2: {}".format(find_range_sum(input_nums, invalid_number)))
