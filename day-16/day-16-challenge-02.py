#!/usr/bin/env python3
""" Advent of Code: Day 16 Challenge 02."""


rules = {}


def deduce_fields(fields):
    identified_fields = 0

    while identified_fields != len(rules):
        matched = {}

        for i, f in fields.items():
            if len(f) == 1:
                matched[i] = f

        for i, f in fields.items():
            if i not in matched:
                for unused, matches in matched.items():
                    fields[i] -= matches

        identified_fields = len(matched)


def validate_field(value):
    valid_fields = []

    for field, constraints in rules.items():
        for constraint in constraints:
            if value >= constraint[0] and value <= constraint[1]:
                valid_fields.append(field)

    return valid_fields


def validate_ticket(ticket_text):
    fields = {}
    values = [int(value.strip()) for value in ticket_text.split(",")]

    for i in range(0, len(values)):
        fields[i] = validate_field(values[i])

    return fields


def add_field(name, valid_ranges):
    rules[name] = valid_ranges


def parse_rule(rule_text):
    name, constraints_text = rule_text.split(":")

    constraints_text = constraints_text.strip()
    constraints = constraints_text.split("or")

    ranges = []

    if len(constraints) <= 1:
        raise ValueError("Parse failed, split on 'or' gave too few values")

    for constraint in constraints:
        constraint.strip()
        min, max = constraint.split("-")

        ranges.append((int(min), int(max)))

    add_field(name, ranges)


if __name__ == "__main__":
    rules_text = ""
    tickets_text = ""

    with open("day-16.rules", "r") as file:
        rules_text = file.readlines()

    with open("day-16.input", "r") as file:
        tickets_text = file.readlines()

    for line in rules_text:
        line = line.strip()

        parse_rule(line)

    combined_fields = {}

    for line in tickets_text[1:]:
        line = line.strip()

        results = validate_ticket(line)

        for index, fields in results.items():
            if index not in combined_fields:
                combined_fields[index] = set([f for f, unused in rules.items()])

            if len(fields) == 0:
                continue

            combined_fields[index] &= set(fields)

    deduce_fields(combined_fields)

    my_ticket = tickets_text[0].split(",")

    result = 1

    for i in range(0, len(my_ticket)):
        if "departure" in str(combined_fields[i]):
            result *= int(my_ticket[i])

    print(f"Value = {result}")
