import utils


def find_missing_seat(all_seats):
    all_ids = {find_id(seat) for seat in all_seats}
    for possible_id in range((127 * 8) + 7):
        if ((set([possible_id - 1, possible_id + 1]) <= all_ids)
                and possible_id not in all_ids):
            return possible_id
    raise ValueError()


def find_id(seat):
    seat = seat.strip()
    row = traverse_binary_space(seat[:7], "F", "B", 0)
    col = traverse_binary_space(seat[7:], "L", "R", 0)
    return (row * 8) + col


def traverse_binary_space(spec, lower_key, upper_key, lower):
    upper = lower + (2 ** len(spec)) - 1
    for key in spec:
        stride = ((upper - lower) + 1) / 2
        if key == lower_key:
            upper -= stride
        elif key == upper_key:
            lower += stride
    return lower


if __name__ == "__main__":
    seat_input = utils.parse_file_lines("day5_input.txt", str)
    print("Part 1: {}".format(max([find_id(seat) for seat in seat_input])))
    print("Part 2: {}".format(find_missing_seat(seat_input)))
