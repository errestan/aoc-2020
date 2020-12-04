#!/usr/bin/env python3
""" Advent of Code: Day 02 Challenge 02."""

if __name__ == "__main__":
    input = ""

    with open("day-02-challenge-01.input", "r") as file:
        input = file.readlines()

    count = 0

    for line in input:
        (possitions, character, password) = line.split(" ")
        (pos_one, pos_two) = possitions.split("-")
        character = character[:1]
        password = password.strip()

        pos_one = int(pos_one) - 1
        pos_two = int(pos_two) - 1
        char_one = password[pos_one]
        char_two = password[pos_two]

        if char_one != char_two and (char_one == character or char_two == character):
            count += 1
            is_valid = "+"
        else:
            is_valid = "-"

        print(f"[{is_valid}] {pos_one + 1} - {pos_two + 1}: {character} - {char_one},{char_two} - {password}")

    print(f"There are {count} valid passwords")
