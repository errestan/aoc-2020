#!/usr/bin/env python3
""" Advent of Code: Day 06 Challenge 01."""


def parse_answers(lines):
    groups = []
    answers = []

    for line in lines:
        line = line.strip()

        if not line:
            print(f"Group: {len(answers)} - {answers}")
            groups.append(answers)
            answers = []
            continue

        answers = answers + [answer for answer in line if answer not in answers]

    return groups


if __name__ == "__main__":
    input = ""

    with open("day-06-challenge-01.input", "r") as file:
        input = file.readlines()

    groups = parse_answers(input)

    total = sum([len(answers) for answers in groups])

    print(f"Total answers: {total}")
