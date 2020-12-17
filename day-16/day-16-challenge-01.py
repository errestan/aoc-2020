#!/usr/bin/env python3
""" Advent of Code: Day 16 Challenge 01."""


fields = {}


def validate_field(value):
    for field, constraints in fields.items():
        for constraint in constraints:
            if value >= constraint[0] and value <= constraint[1]:
                return True

    return False


def validate_ticket(ticket_text):
    invalid_values = []

    for value in ticket_text.split(","):
        value = int(value.strip())

        if not validate_field(value):
            print(f"Adding {value}")
            invalid_values.append(value)

    return invalid_values


def add_field(name, valid_ranges):
    fields[name] = valid_ranges


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

    invalid_values = []

    for line in tickets_text:
        line = line.strip()

        values = validate_ticket(line)
        invalid_values += values

    error_rate = sum([value for value in invalid_values])
    print(f"Error Rate: {error_rate}")
