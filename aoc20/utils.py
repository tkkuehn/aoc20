def parse_file_lines(filepath, parsing_fun):
    with open(filepath) as file_to_parse:
        ints = [parsing_fun(line) for line in file_to_parse]
    return ints
