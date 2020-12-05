#!/usr/bin/env python3
""" Advent of Code: Day 05 Challenge 01."""


def decode_seat(seat):
    if len(seat) != 10:
        raise ValueError(f"Invalid seat: {seat}")

    values = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    onbits = ["B", "b", "R", "r"]
    seatid = 0

    for i in range(0, 10):
        if seat[i] in onbits:
            seatid = seatid + values[i]

    return seatid


if __name__ == "__main__":
    input = ""

    with open("day-05-challenge-01.input", "r") as file:
        input = file.readlines()

    list = sorted([decode_seat(line.strip()) for line in input])

    print(list[0])
    print(list[-1])
