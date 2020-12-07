#!/usr/bin/env python3
""" Advent of Code: Day 07 Challenge 01."""


def parse_colour(string):
    colour = ""

    for word in string.strip().split(" "):
        if word in "bags,bags.bag,bag.":
            break
        elif word.isnumeric():
            continue

        colour = colour + " " + word

    if not colour:
        raise ValueError(f"Invalid colour: {string}")
    return colour.strip()


def parse_rule(rule):
    colour = ""
    contains = []

    bag_colour, bag_contains = rule.split("contain")

    colour = parse_colour(bag_colour)

    for string in bag_contains.split(","):
        if string.strip() == "no other bags.":
            break

        contains.append(parse_colour(string))

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


def can_contain(target, list, bags):
    for colour in list:
        print(f"checking {colour}")
        if colour == target:
            return True
        elif can_contain(target, bags.get(colour), bags):
            return True

    return False


if __name__ == "__main__":
    input = ""

    with open("day-07-challenge-01.input", "r") as file:
        input = file.readlines()

    bags = parse_rules(input)

    results = []

    for bag in bags:
        if bag == "shiny gold":
            continue

        if can_contain("shiny gold", bags[bag], bags):
            results.append(bag)

    print(len(results))
