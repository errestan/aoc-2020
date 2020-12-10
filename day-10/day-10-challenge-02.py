#!/usr/bin/env python3
""" Advent of Code: Day 10 Challenge 02."""


def count(adapters):
    counts = {0: 1}

    for i in adapters:
        counts[i + 1] = counts[i] if i + 1 not in counts else counts[i + 1] + counts[i]
        counts[i + 2] = counts[i] if i + 2 not in counts else counts[i + 2] + counts[i]
        counts[i + 3] = counts[i] if i + 3 not in counts else counts[i + 3] + counts[i]

    return counts[adapters[-1] + 3]


if __name__ == "__main__":
    input = ""

    with open("day-10-challenge-02.input", "r") as file:
        input = file.readlines()

    adapters = [int(i) for i in input]
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    total = count(adapters)

    print(f"Total number of paths is {total}")
