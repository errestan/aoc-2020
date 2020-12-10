#!/usr/bin/env python3
""" Advent of Code: Day 10 Challenge 01."""


if __name__ == "__main__":
    input = ""

    with open("day-10-challenge-01.input", "r") as file:
        input = file.readlines()

    adapters = [int(i) for i in input]
    adapters.sort()
    previous = 0
    count_of_ones = 0
    count_of_threes = 1

    for i in range(0, len(adapters)):
        diff = adapters[i] - previous

        if diff == 0 or diff == 2:
            continue
        elif diff == 1:
            count_of_ones += 1
        elif diff == 3:
            count_of_threes += 1

        previous = adapters[i]

    result = count_of_ones * count_of_threes
    print(f"Result: {result}")
