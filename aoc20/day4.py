import re

import utils


def find_valid_passports(batch):
    valid_passports = 0
    passports = batch.split("\n\n")

    for passport in passports[:-1]:
        if check_passport(passport):
            valid_passports += 1

    return valid_passports


def check_passport(passport_string):
    passport_string = passport_string + "\n"
    regex = r"([a-z]{3}:[a-z0-9#]+\s)" + r"([a-z]{3}:[a-z0-9#]+\s)?" * 7
    fields = re.match(
        regex,
        passport_string).groups()
    fields = set((field[0:3] for field in fields if field is not None))

    return (set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
            <= fields)


def find_valid_passports_2(batch):
    valid_passports = 0
    passports = batch.split("\n\n")

    for passport in passports[:-1]:
        if check_passport(passport) and check_passport_2(passport):
            valid_passports += 1

    return valid_passports


def check_passport_2(passport_string):
    passport_string = passport_string + "\n"
    regex = r"([a-z]{3}:[a-z0-9#]+\s)" + r"([a-z]{3}:[a-z0-9#]+\s)?" * 7
    fields = re.match(
        regex,
        passport_string).groups()
    fields = set((field[:-1] for field in fields if field is not None))
    for field in fields:
        name = field[:3]
        value = field[4:]
        if name == "byr":
            try:
                if not 1920 <= int(value) <= 2002:
                    print("Invalid byr: {}".format(value))
                    return False
            except ValueError:
                print("Non-int byr: {}".format(value))
                return False
        elif name == "iyr":
            try:
                if not 2010 <= int(value) <= 2020:
                    print("Invalid iyr: {}".format(value))
                    return False
            except ValueError:
                print("Non-int byr: {}".format(value))
                return False
        elif name == "eyr":
            try:
                if not 2020 <= int(value) <= 2030:
                    print("Invalid eyr: {}".format(value))
                    return False
            except ValueError:
                print("Non-int eyr: {}".format(value))
                return False
        elif name == "hgt":
            try:
                if value[-2:] == "cm":
                    if not 150 <= int(value[:-2]) <= 193:
                        print("Invalid hgt: {}".format(value))
                        return False
                elif value[-2:] == "in":
                    if not 59 <= int(value[:-2]) <= 76:
                        print("Invalid hgt: {}".format(value))
                        return False
                else:
                    return False
            except ValueError:
                print("Non-int hgt: {}".format(value))
                return False
        elif name == "hcl":
            if re.fullmatch(r"#[a-f0-9]{6}", value) is None:
                print("Invalid hcl: {}".format(value))
                return False
        elif name == "ecl":
            if value not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                print("Invalid ecl: {}".format(value))
                return False
        elif name == "pid":
            if re.fullmatch(r"[0-9]{9}", value) is None:
                print("Invalid pid: {}".format(value))
                return False
        elif name == "cid":
            continue
        else:
            print("Invalid key: {}".format(name))
            return False
    return True


if __name__ == "__main__":
    batch_input = "".join(utils.parse_file_lines("day4_input.txt", str)) + "\n"
    print("Part 1: {}".format(find_valid_passports(batch_input)))
    print("Part 2: {}".format(find_valid_passports_2(batch_input)))
