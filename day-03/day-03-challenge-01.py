#!/usr/bin/env python3
""" Advent of Code 2020: Day 03 Challenge 01."""

if __name__ == "__main__":
    input = ""

    with open("day-03-challenge-01.input", "r") as file:
        input = file.readlines()

    board = [list(row.strip()) for row in input]

    steps_down = 1
    steps_right = 3

    count = 0
    x = 0
    y = 0

    for row in board:
        cell = row[x]

        if cell == "#":
            count = count + 1
            row[x] = "X"
        else:
            row[x] = "O"

        print(f"{str(row)[1:-1]}")

        y = y + steps_down
        x = (y * steps_right) % len(row)

    print(f"There {count} trees on your path.")
