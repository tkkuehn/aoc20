import re

import utils

def find_valid_passwords(password_strings):
    valid_passwords = 0

    for password_string in password_strings:
        if check_password(password_string):
            valid_passwords += 1

    return valid_passwords

def find_valid_passwords_2(password_strings):
    valid_passwords = 0

    for password_string in password_strings:
        if check_password_2(password_string):
            valid_passwords += 1

    return valid_passwords

def check_password(password_string):
    min_letters, max_letters, policy_letter, password = re.match(
        r"(\d+)-(\d+) ([a-z]): ([a-z]+)",
        password_string).groups()
    min_letters = int(min_letters)
    max_letters = int(max_letters)
    num_letters = password.count(policy_letter)

    return min_letters <= num_letters <= max_letters

def check_password_2(password_string):
    position_1, position_2, policy_letter, password = re.match(
        r"(\d+)-(\d+) ([a-z]): ([a-z]+)",
        password_string).groups()
    position_1 = int(position_1) - 1
    position_2 = int(position_2) - 1

    return ((password[position_1] == policy_letter)
            ^ (password[position_2] == policy_letter))

if __name__ == "__main__":
    parsed_strings = utils.parse_file_lines("day2_input.txt", str)
    print("Part 1: {}".format(find_valid_passwords(parsed_strings)))
    print("Part 2: {}".format(find_valid_passwords_2(parsed_strings)))
