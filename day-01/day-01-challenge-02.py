#!/usr/bin/env python3
""" Advent of Code 2020: Day 01 Challenge 02."""


if __name__ == "__main__":
    input = ""

    with open("day-01-challenge-01.input", "r") as file:
        input = file.readlines()

    input_list = [int(line.strip()) for line in input]

    for i in input_list:
        for j in input_list:
            for k in input_list:
                if i + j + k == 2020:
                    print(f"{i} + {j} + {k} = 2020, {i} * {j} * {k} = {i * j * k}")
