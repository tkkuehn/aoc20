import utils


def find_all_answers(groups):
    return [len(find_answers(group)) for group in groups]


def find_all_common_answers(groups):
    return [len(find_common_answers(group)) for group in groups]


def find_answers(group):
    all_answers = set()
    for person in group:
        all_answers |= set(person)
    return all_answers


def find_common_answers(group):
    common_answers = set(group[0])
    for person in group:
        common_answers &= set(person)
    return common_answers


if __name__ == "__main__":
    input_groups = utils.parse_file_groups("day6_input.txt")
    print("Part 1: {}".format(sum(find_all_answers(input_groups))))
    print("Part 2: {}".format(sum(find_all_common_answers(input_groups))))
