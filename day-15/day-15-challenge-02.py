#!/usr/bin/env python3
""" Advent of Code: Day 15 Challenge 02."""


# Might have missed the point here. No changes from part 1. It took a few moments to compute but no more than
# 30 seconds. There may be a more efficient way of doing it.
if __name__ == "__main__":
    input = ""

    with open("day-15.input", "r") as file:
        input = file.readlines()

    previous = {}
    current = 0
    round = 1
    last = -1

    for number in input[0].split(","):
        current = int(number.strip())

        if last >= 0:
            previous[last] = round

        round += 1
        last = current

    for i in range(round, 30000001):
        if last in previous:
            diff = round - previous[last]
            current = diff
        else:
            current = 0

        previous[last] = round
        round += 1
        last = current

    print(f"The last number was: {last}")
