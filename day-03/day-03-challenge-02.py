#!/usr/bin/env python3
""" Advent of Code 2020: Day 03 Challenge 01."""


def count_trees(board, steps_right, steps_down):
    count = 0
    max_y = len(board)
    max_x = len(board[0])
    x = 0

    for y in range(0, max_y, steps_down):
        cell = board[y][x]

        if cell == "#":
            count = count + 1

        x = (x + steps_right) % max_x

    return count


if __name__ == "__main__":
    input = ""

    with open("day-03-challenge-02.input", "r") as file:
        input = file.readlines()

    board = [list(row.strip()) for row in input]
    total = 1

    for y in range(1, 3):
        for x in range(1, 14 - (y * 6), 2):
            count = count_trees(board, x, y)
            total = total * count
            print(f"Right {x}, Down {y} = {count} -- {total}")

    print(f"The total is: {total}.")
