import re

import utils


def parse_line(line):
    mask_re = r"mask = ([10X]{36})"
    mem_re = r"mem\[(\d+)\] = (\d+)"
    mask_match = re.fullmatch(mask_re, line)
    if mask_match is not None:
        mask_str = mask_match.group(1)
        or_int = int(mask_str.replace("X", "0"), 2)
        and_int = int(mask_str.replace("X", "1"), 2)
        return True, or_int, and_int
    mem_match = re.fullmatch(mem_re, line)
    if mem_match is not None:
        return False, int(mem_match.group(1)), int(mem_match.group(2))
    raise ValueError(f"Could not parse line {line}")


def parse_line_2(line):
    mask_re = r"mask = ([10X]{36})"
    mem_re = r"mem\[(\d+)\] = (\d+)"
    mask_match = re.fullmatch(mask_re, line)
    if mask_match is not None:
        return True, mask_match.group(1), None
    mem_match = re.fullmatch(mem_re, line)
    if mem_match is not None:
        return False, int(mem_match.group(1)), int(mem_match.group(2))
    raise ValueError(f"Could not parse line {line}")


def apply_bitmask(bitmask, addr):
    addr_str = format(addr, "036b")
    out_addr = []
    for mask_val, addr_val in zip(bitmask, addr_str):
        if mask_val == "0":
            out_addr.append(addr_val)
        if mask_val in ["1", "X"]:
            out_addr.append(mask_val)
    return "".join(out_addr)


def enumerate_addrs(addr_spec, out_addrs):
    new_addrs = []
    char = addr_spec[0]
    if char in ["0", "1"]:
        for out_addr in out_addrs:
            new_addrs.append(out_addr + char)
        if len(out_addrs) == 0:
            new_addrs.append(char)
    elif char == "X":
        for out_addr in out_addrs:
            new_addrs.extend([out_addr + "0", out_addr + "1"])
        if len(out_addrs) == 0:
            new_addrs.extend(["0", "1"])
    if len(addr_spec) == 1:
        return new_addrs
    return enumerate_addrs(addr_spec[1:], new_addrs)


def initialize(program):
    mask_or, mask_and = 0, 2*35
    memory = {}
    for line in program:
        update_mask, int_1, int_2 = parse_line(line.strip())
        if update_mask:
            mask_or = int_1
            mask_and = int_2
        else:
            addr = int_1
            val = int_2
            memory[addr] = (val | mask_or) & mask_and
    return sum(memory.values())


def initialize_2(program):
    mask = format(0, "036b")
    memory = {}
    for line in program:
        update_mask, val_1, int_2 = parse_line_2(line.strip())
        if update_mask:
            mask = val_1
        else:
            addr_spec = apply_bitmask(mask, val_1)
            addrs = enumerate_addrs(addr_spec, [])
            for addr in addrs:
                memory[addr] = int_2
    return sum(memory.values())


if __name__ == "__main__":
    input_program = utils.parse_file_lines("day14_input.txt", str)
    print("Part 1: {}".format(initialize(input_program)))
    print("Part 2: {}".format(initialize_2(input_program)))
