#!/usr/bin/env python3
""" Advent of Code: Day 11 Challenge 02."""


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

    y_min = 0
    y_max = len(seat_plan)
    x_min = 0
    x_max = len(seat_plan[0])

    nearest_seats = {"ul": ".", "up": ".", "ur": ".", "lt": ".", "rt": ".", "dl": ".", "dn": ".", "dr": "."}

    for j in range(1, y_max):
        up = y + j
        dn = y - j
        rt = x + j
        lt = x - j

        if dn >= y_min and lt >= x_min and nearest_seats["dl"] == ".":
            nearest_seats["dl"] = seat_plan[dn][lt]
        if dn >= y_min and rt < x_max and nearest_seats["dr"] == ".":
            nearest_seats["dr"] = seat_plan[dn][rt]
        if up < y_max and lt >= x_min and nearest_seats["ul"] == ".":
            nearest_seats["ul"] = seat_plan[up][lt]
        if up < y_max and rt < x_max and nearest_seats["ur"] == ".":
            nearest_seats["ur"] = seat_plan[up][rt]

        if dn >= y_min and nearest_seats["dn"] == ".":
            nearest_seats["dn"] = seat_plan[dn][x]
        if up < y_max and nearest_seats["up"] == ".":
            nearest_seats["up"] = seat_plan[up][x]
        if lt >= x_min and nearest_seats["lt"] == ".":
            nearest_seats["lt"] = seat_plan[y][lt]
        if rt < x_max and nearest_seats["rt"] == ".":
            nearest_seats["rt"] = seat_plan[y][rt]

    for direction, state in nearest_seats.items():
        if state == "#":
            occupied += 1

    if occupied == 0 and seat_plan[y][x] == "L":
        return True
    elif occupied >= 5 and seat_plan[y][x] == "#":
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

    seat_plan_new = update_seat_plan(seat_plan_old)

    while not compare_seat_plans(seat_plan_old, seat_plan_new):
        seat_plan_old = seat_plan_new
        seat_plan_new = update_seat_plan(seat_plan_old)
        # print_seat_plan(seat_plan_new)

    count = count_occupied(seat_plan_new)
    print(f"There are {count} occupied seat(s).")
