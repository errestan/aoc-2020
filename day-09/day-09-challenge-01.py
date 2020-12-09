#!/usr/bin/env python3
""" Advent of Code: Day 08 Challenge 01."""


def is_sum_of(sum, start, end, data):
    for i in range(start, end):
        for j in range(start, end):
            if i == j:
                continue

            if data[i] + data[j] == sum:
                return True

    return False


if __name__ == "__main__":
    input = ""

    with open("day-09-challenge-01.input", "r") as file:
        input = file.readlines()

    preamble_len = 25

    stream = [int(number) for number in input]
    length = len(stream)

    for i in range(25, length - 1):
        sum = stream[i]
        min = i - preamble_len
        max = i

        if not is_sum_of(sum, min, max, stream):
            raise ValueError(f"{sum} is not the of any of the previous {preamble_len} numbers.")
