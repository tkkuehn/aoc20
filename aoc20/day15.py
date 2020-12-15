import utils


def play_game(starting_num_str, iterations):
    starting_nums = [int(num) for num in starting_num_str.strip().split(",")]
    ages = {}
    last_spoken = None
    first_time = False
    diff = None
    for turn_idx in range(iterations):
        if turn_idx < len(starting_nums):
            last_spoken = starting_nums[turn_idx]
        elif first_time:
            last_spoken = 0
        else:
            last_spoken = diff
        first_time = last_spoken not in ages.keys()
        if not first_time:
            diff = turn_idx - ages[last_spoken]
        ages[last_spoken] = turn_idx
    return last_spoken


if __name__ == "__main__":
    input_nums = utils.parse_file_lines("day15_input.txt", str)[0]
    print("Part 1: {}".format(play_game(input_nums, 2020)))
    print("Part 2: {}".format(play_game(input_nums, 30000000)))
