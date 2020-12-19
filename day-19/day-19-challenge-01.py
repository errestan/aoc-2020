#!/usr/bin/env python3
""" Advent of Code: Day 19 Challenge 01."""

rules = {}


def parse_rule(message, start, rule_num):
    res = True
    pos = start

    for element in rules[rule_num]:
        # print(f"{pos} : {element}")
        element = element.strip('"')

        if element.isnumeric():
            if res:
                index = int(element)

                pos, res = parse_rule(message, pos, index)
                continue
        elif element == "|":
            if res:
                break
            else:
                pos = start
                res = True
                continue
        else:
            if pos < len(message):
                # print(f"{message[pos]} == {element}")
                res = True if message[pos] == element else False
            else:
                break

        pos += 1

    return (pos, res)


if __name__ == "__main__":
    rules_text = ""

    with open("day-19-challenge-01.rules", "r") as file:
        rules_text = file.readlines()

    for line in rules_text:
        num, txt = line.strip().split(":")

        rules[int(num)] = txt.strip().split(" ")

    message_text = ""

    with open("day-19.input", "r") as file:
        message_text = file.readlines()

    count = 0

    for message in message_text:
        message = message.strip()
        print(message)

        pos, result = parse_rule(message, 0, 0)

        if pos != len(message):
            result = False

        if result:
            count += 1

        # print("Valid" if result else "Invalid")

    print(f"The number of valid message(s) is {count}")
