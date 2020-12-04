#!/usr/bin/enve python3
""" Advent of Code 2020: Day 04 Challenge 01."""

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_valid(fields):
    for field in required_fields:
        if field not in fields:
            return False

    return True


def parse_passport(lines):
    fields = {}

    for line in lines:
        line = line.strip()

        pairs = line.split(" ")

        for pair in pairs:
            key, value = pair.split(":")
            fields[key] = value

    return fields


if __name__ == "__main__":
    input = ""

    with open("day-04-challenge-01.input", "r") as file:
        input = file.readlines()

    entries = []
    lines = []
    total = 0

    for line in input:
        line = line.strip()

        if line == "":
            total = total + 1
            entries.append(lines)
            lines = []
            continue

        lines.append(line)

    count = 0

    for lines in entries:
        fields = parse_passport(lines)

        count = count + 1 if is_valid(fields) else count

    print(f"There are {count} valid passports out of {total}")
