#!/usr/bin/env python3
""" Advent of Code: Day 02 Challenge 01."""

if __name__ == "__main__":
    input = ""

    with open("day-02-challenge-01.input", "r") as file:
        input = file.readlines()

    count = 0

    for line in input:
        (range, character, password) = line.split(" ")
        (min, max) = range.split("-")
        character = character[:1]
        password = password.strip()

        instances = password.count(character)

        if instances >= int(min) and instances <= int(max):
            count += 1
            is_valid = "+"
        else:
            is_valid = "-"

        print(f"[{is_valid}] {min} - {max}: {character} - {password}")

    print(f"There are {count} valid passwords")
