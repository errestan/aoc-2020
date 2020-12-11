#!/usr/bin/env python3
""" Advent of Code: Day 11 Challenge 01."""


def count_occupied(seat_plan):
    count = 0

    for row in seat_plan:
        for seat in row:
            if seat == "#":
                count += 1

    return count


def print_seat_plan(seat_plan):
    for y in range(0, len(seat_plan)):
        for x in range(0, len(seat_plan[0])):
            print(f"{seat_plan[y][x]}", end="")

        print("")

    print("")


def toggle_seat(seat_plan, y, x):
    if seat_plan[y][x] == "L":
        seat_plan[y][x] = "#"
    elif seat_plan[y][x] == "#":
        seat_plan[y][x] = "L"
    else:
        raise ValueError("Invalid seat state, can't toggle.")


def check_seat(seat_plan, y, x):
    occupied = 0

    for j in range(y - 1, y + 2):
        if j < 0 or j >= len(seat_plan):
            continue

        for i in range(x - 1, x + 2):
            if i < 0 or i >= len(seat_plan[0]):
                continue

            if j == y and i == x:
                continue

            if seat_plan[j][i] == "#":
                occupied += 1

    if occupied == 0 and seat_plan[y][x] == "L":
        return True
    elif occupied >= 4 and seat_plan[y][x] == "#":
        return True

    return False


def copy_seat_plan(old):
    new = []

    for y in old:
        new_row = []

        for x in y:
            new_row.append(x)

        new.append(new_row)

    return new


def update_seat_plan(old_seat_plan):
    new_seat_plan = copy_seat_plan(old_seat_plan)

    for y in range(0, len(old_seat_plan)):
        for x in range(0, len(old_seat_plan[0])):
            if old_seat_plan[y][x] == ".":
                continue

            if check_seat(old_seat_plan, y, x):
                toggle_seat(new_seat_plan, y, x)

    return new_seat_plan


def compare_seat_plans(first, second):
    for y in range(0, len(first)):
        for x in range(0, len(first[0])):
            if first[y][x] != second[y][x]:
                return False

    print("No change")
    return True


def parse_seat_plan(input):
    seat_plan = []

    for line in input:
        line.strip("\n")

        seat_row = []

        for seat in line:
            seat.strip()

            if seat not in ["#", ".", "L"]:
                if seat == "\n":
                    continue

                raise ValueError(f"Invalid seat state: {seat}")

            seat_row.append(seat)

        seat_plan.append(seat_row)

    return seat_plan


if __name__ == "__main__":
    input = ""

    with open("day-11.input", "r") as file:
        input = file.readlines()

    seat_plan_old = parse_seat_plan(input)
    # print_seat_plan(seat_plan_old)

    seat_plan_new = update_seat_plan(seat_plan_old)
    # print_seat_plan(seat_plan_new)

    while not compare_seat_plans(seat_plan_old, seat_plan_new):
        seat_plan_old = seat_plan_new
        seat_plan_new = update_seat_plan(seat_plan_old)

    count = count_occupied(seat_plan_new)
    print(f"There are {count} occupied seat(s).")
