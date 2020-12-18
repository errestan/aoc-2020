#!/usr/bin/env python3
""" Advent of Code: Day 17 Challenge 01."""


def get_state(x, y, z, space):
    if not space.get(x):
        space[x] = {}

    if y not in space[x]:
        space[x][y] = {}

    if z not in space[x][y]:
        space[x][y][z] = "."

    return space[x][y][z]


def set_state(x, y, z, state, space):
    value = get_state(x, y, z, space)

    if state != value:
        space[x][y][z] = state


def count_active_neighbours(x, y, z, space):
    count = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if i == x and j == y and k == z:
                    continue

                if get_state(i, j, k, space) == "#":
                    count += 1

    return count


def apply_active(x, y, z, space):
    active_neigbours = count_active_neighbours(x, y, z, space)

    return "#" if active_neigbours == 2 or active_neigbours == 3 else "."


def apply_inactive(x, y, z, space):
    active_neigbours = count_active_neighbours(x, y, z, space)

    return "#" if active_neigbours == 3 else "."


def apply_cycle(space):
    new_space = {}

    x_min = min([x for x, unused in space.items()]) - 1
    y_min = min([y for y, unused in space[0].items()]) - 1
    z_min = min([z for z, unused in space[0][0].items()]) - 1

    x_max = max([x for x, unused in space.items()]) + 2
    y_max = max([y for y, unused in space[0].items()]) + 2
    z_max = max([z for z, unused in space[0][0].items()]) + 2

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            for z in range(z_min, z_max):
                current = get_state(x, y, z, space)

                if current == "#":
                    set_state(x, y, z, apply_active(x, y, z, space), new_space)
                elif current == ".":
                    set_state(x, y, z, apply_inactive(x, y, z, space), new_space)

    return new_space


def print_layer(space, z):
    x_min = min([x for x, unused in space.items()])
    y_min = min([y for y, unused in space[0].items()])

    x_max = max([x for x, unused in space.items()]) + 1
    y_max = max([y for y, unused in space[0].items()]) + 1

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            print(f"{get_state(x, y, z, space)}", end="")

        print()


def count_active(space):
    count = 0

    for key_x, value_x in space.items():
        for key_y, value_y in value_x.items():
            for key_z, value_z in value_y.items():
                if value_z == "#":
                    count += 1

    return count


if __name__ == "__main__":
    input = ""

    with open("day-17.input", "r") as file:
        input = file.readlines()

    space = {}
    x_pos = 0

    for line in input:
        y_pos = 0

        for char in line.strip():
            set_state(x_pos, y_pos, 0, char, space)
            y_pos += 1

        x_pos += 1

    for cycle in range(6):
        space = apply_cycle(space)

    result = count_active(space)
    print(f"There are {result} active cubes.")
