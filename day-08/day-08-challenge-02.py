#!/usr/bin/env python3
""" Advent of Code: Day 08 Challenge 02."""

valid_ops = ["acc", "jmp", "nop"]


def toggle_instruction(instructions, address):
    if address < 0 or address >= len(instructions):
        raise ValueError(f"Address {address} is outside the bounds of the program.")

    if instructions[address][0] == "jmp":
        instructions[address][0] = "nop"
    elif instructions[address][0] == "nop":
        instructions[address][0] = "jmp"
    else:
        raise ValueError(f"Invalid instruction {instructions[address]}")


def execute(instrcutions):
    cir = 0
    acc = 0

    # Reset the run status of each instructions.
    for i in range(0, len(instructions)):
        instructions[i][2] = False

    while cir >= 0 and cir < len(instructions):
        if instructions[cir][2]:
            raise RuntimeError(f"Infinite loop detected: {cir}")

        op, val = instructions[cir][:-1]
        instructions[cir][2] = True

        if op == "acc":
            acc += val
        elif op == "jmp":
            cir += val
            continue
        elif op == "nop":
            pass
        else:
            raise ValueError(f"Invalid instruction {op}")

        cir += 1

    return acc


def fix_instructions(instructions):
    result = 0

    for idx in range(0, len(instructions)):
        if instructions[idx][0] not in ["jmp", "nop"]:
            continue

        toggle_instruction(instructions, idx)

        try:
            result = execute(instructions)

            print(f"Success {result}")
        except RuntimeError:
            # Put the instruction back.
            toggle_instruction(instructions, idx)
            continue

        break

    return result


if __name__ == "__main__":
    input = ""

    with open("day-08-challenge-01.input", "r") as file:
        input = file.readlines()

    instructions = []

    for line in input:
        op, val = line.strip().split(" ")

        if op not in valid_ops:
            raise ValueError(f"Invalid instruction {op}")

        # if val.startswith("+"):
        #     val = val[1:]

        if not val[1:].isnumeric():
            raise ValueError(f"Invalid value {val} is not a number.")

        instructions.append([op, int(val), False])

    print(f"Parsed {len(instructions)} instructions")

    result = fix_instructions(instructions)

    print(f"The final value was: {result}")
