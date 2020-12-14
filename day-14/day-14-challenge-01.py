#!/usr/bin/env python3
""" Advent of Code: Day 14 Challenge 01."""


memory = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def apply_mask(value):
    if len(mask) != 36:
        raise ValueError(f"Invalid mask length: {len(mask)}")

    for i in range(0, 36):
        if mask[i] == "X" or mask[i] == "x":
            continue
        elif mask[i] == "0":
            value &= ~(2 ** (35 - i))
        elif mask[i] == "1":
            value |= 2 ** (35 - i)
        else:
            raise ValueError(f"Invalid mask character: {mask[i]}")

    return value


def write_memory(address, value):
    memory[address] = apply_mask(value)


def read_memory(address):
    if address not in memory:
        raise ValueError(f"Invalid memory address: {address}")

    return memory[address]


if __name__ == "__main__":
    input = ""

    with open("day-14.input", "r") as file:
        input = file.readlines()

    for line in input:
        line = line.strip()

        cmd, arg = line.split("=")

        if cmd.strip() == "mask":
            mask = arg.strip()
        elif cmd.startswith("mem"):
            addr_start = cmd.index("[") + 1
            addr_end = cmd.index("]")
            addr = int(cmd[addr_start:addr_end])

            write_memory(addr, int(arg))

    total = sum([value for address, value in memory.items()])
    print(total)
