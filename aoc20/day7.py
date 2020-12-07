import re
from collections import defaultdict

import utils


def count_bags(relationship_map, colour):
    num_bags = 0
    for child in relationship_map[colour]["contains"]:
        num_bags += child[0]
        num_bags += child[0] * count_bags(relationship_map, child[1])
    return num_bags


def find_parents(relationship_map, colour, parents):
    for parent in relationship_map[colour]["contained by"]:
        parents.add(parent[1])
        if len(relationship_map[parent[1]]["contained by"]) > 0:
            find_parents(relationship_map, parent[1], parents)


def parse_all_lines(luggage_spec):
    relationship_map = defaultdict(lambda: defaultdict(list))
    for line in luggage_spec:
        parse_line(line.strip(), relationship_map)
    return relationship_map


def parse_line(spec_string, relationship_map):
    content_match = re.fullmatch(
        r"([a-z ]+) bags contain ((?:\d+ [a-z ]+ bags?(?:, )?)+)\.",
        spec_string)
    if content_match is None:
        return
    bag, contents = content_match.groups()
    contents = contents.strip().split(", ")
    contents = [re.fullmatch(r"(\d+) ([a-z ]+) bags?,?", content).groups()
                for content in contents]
    contents = [(int(content[0]), content[1]) for content in contents]

    for content in contents:
        relationship_map[bag]["contains"].append(content)
        relationship_map[content[1]]["contained by"].append((content[0], bag))


if __name__ == "__main__":
    spec = utils.parse_file_lines("day7_input.txt", str)
    input_map = parse_all_lines(spec)
    gold_parents = set()
    find_parents(input_map, "shiny gold", gold_parents)
    print("Part 1: {}".format(len(gold_parents)))
    print("Part 2: {}".format(count_bags(input_map, "shiny gold")))
