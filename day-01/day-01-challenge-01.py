#!/usr/bin/env python3
""" Advent of Code 2020: Day 01 Challenge 01."""


if __name__ == "__main__":
    input = ""

    with open("day-01-challenge-01.input", "r") as file:
        input = file.readlines()

    input_list = [int(line.strip()) for line in input]

    for number in input_list:
        candidate = 2020 - number

        if candidate in input_list:
            print(f"{number} * {candidate} = {number * candidate}")
