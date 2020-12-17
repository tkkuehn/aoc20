import re

import utils


def parse_rule(rule_str):
    rule_re = r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)"
    match = re.fullmatch(rule_re, rule_str)
    field = match.group(1)
    range_1 = range(int(match.group(2)), int(match.group(3)) + 1)
    range_2 = range(int(match.group(4)), int(match.group(5)) + 1)
    return field, range_1, range_2


def check_ticket(ticket_str, rules):
    invalid_values = []
    for num in [int(num_str) for num_str in ticket_str.split(",")]:
        num_valid = False
        for rule in rules:
            if (num in rule[1]) or (num in rule[2]):
                num_valid = True
                break
        if not num_valid:
            invalid_values.append(num)
    return invalid_values


def find_error_rate(input_str):
    rule_strs, yours, nearby = input_str.strip().split("\n\n")
    rules = [
        parse_rule(rule_str.strip()) for rule_str in rule_strs.split("\n")]
    invalid_nums = []
    for ticket in nearby.split("\n")[1:]:
        invalid_nums += check_ticket(ticket.strip(), rules)
    return sum(invalid_nums)


def identify_fields(input_str):
    rule_strs, yours, nearby = input_str.strip().split("\n\n")
    rules = [
        parse_rule(rule_str.strip()) for rule_str in rule_strs.split("\n")]
    tickets = [ticket.strip() for ticket in nearby.split("\n")[1:]]
    possibilities = [set(rules) for field in tickets[0].split(",")]
    for ticket in tickets:
        if len(check_ticket(ticket, rules)) > 0:
            continue
        for field_idx, field in enumerate(ticket.split(",")):
            field_int = int(field)
            current_possibilities = possibilities[field_idx].copy()
            for possibility in current_possibilities:
                if ((field_int not in possibility[1])
                        and (field_int not in possibility[2])):
                    possibilities[field_idx].remove(possibility)
    possibilities = [
        {rule[0] for rule in possibility} for possibility in possibilities
        ]
    while (sum([len(possibility_set) for possibility_set in possibilities])
            > len(possibilities)):
        singletons = []
        for idx, possibility_set in enumerate(possibilities):
            if len(possibility_set) == 1:
                singletons.append((idx, list(possibility_set)[0]))
        for singleton in singletons:
            for idx, possibility_set in enumerate(possibilities.copy()):
                if idx != singleton[0] and singleton[1] in possibilities[idx]:
                    possibilities[idx].remove(singleton[1])
    your_ticket = [
        int(num) for num in yours.split("\n")[1].strip().split(",")
    ]
    return (
        your_ticket,
        [list(possibility)[0] for possibility in possibilities]
    )


if __name__ == "__main__":
    input_spec = "".join(utils.parse_file_lines("day16_input.txt", str))
    print("Part 1: {}".format(find_error_rate(input_spec)))
    your_tkt, field_names = identify_fields(input_spec)
    acc = 1
    for idx, field in enumerate(field_names):
        if field.startswith("departure"):
            acc *= your_tkt[idx]
    print("Part 2: {}".format(acc))
