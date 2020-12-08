import utils


def acc(arg, acc, ptr):
    return (acc + arg, ptr + 1)


def nop(arg, acc, ptr):
    return (acc, ptr + 1)


def jmp(arg, acc, ptr):
    return (acc, ptr + arg)


instruction_map = {"acc": acc, "jmp": jmp, "nop": nop}


def parse_instruction(ins_str):
    ins = ins_str[:3]
    arg = int(ins_str[4:])
    return (ins, arg)


def execute_code(program):
    ptr = 0
    acc = 0
    executed_ptrs = set()
    terminated = False
    while ptr < len(program):
        ins, arg = parse_instruction(program[ptr])
        if ptr in executed_ptrs:
            break
        executed_ptrs.add(ptr)
        acc, ptr = instruction_map[ins](arg, acc, ptr)
    if ptr == len(program):
        terminated = True
    return acc, terminated


def change_code(program):
    for ptr, line in enumerate(program):
        ins, arg = parse_instruction(line)
        if ins in ["nop", "jmp"]:
            program_copy = program.copy()
            if ins == "nop":
                program_copy[ptr] = "jmp" + program_copy[ptr][3:]
            else:
                program_copy[ptr] = "nop" + program_copy[ptr][3:]
            acc, terminated = execute_code(program_copy)
            if terminated:
                return acc


if __name__ == "__main__":
    program = utils.parse_file_lines("day8_input.txt", str)
    program = [line.strip() for line in program]
    print("Part 1: {}".format(execute_code(program)[0]))
    print("Part 2: {}".format(change_code(program)))
