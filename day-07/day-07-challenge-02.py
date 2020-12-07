#!/usr/bin/env python3
""" Advent of Code: Day 07 Challenge 02."""


def parse_colour(string):
    colour = ""
    count = 0

    for word in string.strip().split(" "):
        if word in "bags,bags.bag,bag.":
            break
        elif word.isnumeric():
            count = int(word)
            continue

        colour = colour + " " + word

    if not colour:
        raise ValueError(f"Invalid colour: {string}")

    return (colour.strip(), count)


def parse_rule(rule):
    colour = ""
    contains = {}

    bag_colour, bag_contains = rule.split("contain")

    colour = parse_colour(bag_colour)[0]

    for string in bag_contains.split(","):
        if string.strip() == "no other bags.":
            break

        bag_colour, bag_count = parse_colour(string)
        contains[bag_colour] = bag_count

    return (colour, contains)


def parse_rules(rules):
    bags = {}

    for line in rules:
        (colour, list) = parse_rule(line)

        if colour in bags:
            print(f"Duplicate colour: {colour}")
            continue

        bags[colour] = list

    return bags


def contains(contents, bags):
    total = 0

    for bag in contents:
        number = contents[bag]
        total = total + number
        total = total + number * contains(bags[bag], bags)

    return total


if __name__ == "__main__":
    input = ""

    with open("day-07-challenge-02.input", "r") as file:
        input = file.readlines()

    bags = parse_rules(input)
    total = contains(bags["shiny gold"], bags)

    print(f"A shiny gold bag must contain: {total} bags.")
