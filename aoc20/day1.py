import utils

def find_sum_2(nums, expected_sum):
    for i, num1 in enumerate(nums):
        for num2 in nums[i + 1:]:
            if num1 + num2 == expected_sum:
                return num1 * num2
    raise Exception("No pair summed to {}".format(expected_sum))

def find_sum_3(nums, expected_sum):
    for i, num1 in enumerate(nums):
        for num2 in nums[i + 1:]:
            for num3 in nums[i + 2:]:
                if num1 + num2 + num3 == expected_sum:
                    return num1 * num2 * num3
    raise Exception("No triplet summed to {}".format(expected_sum))

if __name__ == "__main__":
    input_nums = utils.parse_file_lines("aoc20/day1_input.txt", int)
    print("Part 1: {}".format(find_sum_2(input_nums, 2020)))
    print("Part 2: {}".format(find_sum_3(input_nums, 2020)))
