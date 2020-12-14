#!/usr/bin/env python3
""" Advent of Code: Day 14 Challenge 02."""


memory = {}
mask = "0" * 36


def apply_mask(address):
    if len(mask) != 36:
        raise ValueError(f"Invalid mask length: {len(mask)}")

    floating_bits = []

    for i in range(0, 36):
        if mask[i] == "0":
            continue
        elif mask[i] == "X" or mask[i] == "x":
            floating_bits.append(35 - i)
            address &= ~(2 ** (35 - i))
        elif mask[i] == "1":
            address |= 2 ** (35 - i)
        else:
            raise ValueError(f"Invalid mask character: {mask[i]}")

    addresses = []

    for i in range(0, 2 ** len(floating_bits)):
        floating_mask = 0

        for bit in range(0, len(floating_bits)):
            if i & (1 << bit) == 1 << bit:
                floating_mask |= 1 << floating_bits[bit]

        addresses.append(address | floating_mask)

    return addresses


def write_memory(address, value):
    addresses = apply_mask(address)

    if not address:
        raise ValueError("No address(s)")

    for a in addresses:
        memory[a] = value


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
