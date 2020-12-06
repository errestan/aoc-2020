#!/usr/bin/env python3
""" Advent of Code: Day 06 Challenge 02."""


def parse_answers(lines):
    groups = []
    answers = {}
    count = 0

    for line in lines:
        line = line.strip()

        if not line:
            common = [answer for answer, value in answers.items() if value == count]
            groups.append(common)
            answers = {}

            print(f"Group: {count} -- {common}")

            count = 0
            continue

        count = count + 1

        for answer in line:
            if answer in answers.keys():
                answers[answer] = answers[answer] + 1
            else:
                answers[answer] = 1

    return groups


if __name__ == "__main__":
    input = ""

    with open("day-06-challenge-02.input", "r") as file:
        input = file.readlines()

    groups = parse_answers(input)

    total = sum([len(answers) for answers in groups])

    print(f"Total answers: {total}")
