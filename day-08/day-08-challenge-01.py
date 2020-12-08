#!/usr/bin/env python3
""" Advent of Code: Day 08 Challenge 01."""

valid_ops = ["acc", "jmp", "nop"]


def execute(instrcutions):
    cir = 0
    acc = 0

    while not instructions[cir][2]:
        op, val = instructions[cir][:-1]
        instructions[cir][2] = True

        if op == "acc":
            acc += val
            cir += 1
        elif op == "jmp":
            cir += val
        elif op == "nop":
            cir += 1
            continue
        else:
            raise ValueError(f"Invalid instruction {op}")

    return acc


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

    result = execute(instructions)

    print(f"The final value was: {result}")
