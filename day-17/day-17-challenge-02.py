#!/usr/bin/env python3
""" Advent of Code: Day 17 Challenge 02."""


def get_state(x, y, z, w, space):
    if not space.get(x):
        space[x] = {}

    if y not in space[x]:
        space[x][y] = {}

    if z not in space[x][y]:
        space[x][y][z] = {}

    if w not in space[x][y][z]:
        space[x][y][z][w] = "."

    return space[x][y][z][w]


def set_state(x, y, z, w, state, space):
    value = get_state(x, y, z, w, space)

    if state != value:
        space[x][y][z][w] = state


def count_active_neighbours(x, y, z, w, space):
    count = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for m in range(w - 1, w + 2):
                    if i == x and j == y and k == z and m == w:
                        continue

                    if get_state(i, j, k, m, space) == "#":
                        count += 1

    return count


def apply_active(x, y, z, w, space):
    active_neigbours = count_active_neighbours(x, y, z, w, space)

    return "#" if active_neigbours == 2 or active_neigbours == 3 else "."


def apply_inactive(x, y, z, w, space):
    active_neigbours = count_active_neighbours(x, y, z, w, space)

    return "#" if active_neigbours == 3 else "."


def apply_cycle(space):
    new_space = {}

    x_min = min([x for x, unused in space.items()]) - 1
    y_min = min([y for y, unused in space[0].items()]) - 1
    z_min = min([z for z, unused in space[0][0].items()]) - 1
    w_min = min([w for w, unused in space[0][0][0].items()]) - 1

    x_max = max([x for x, unused in space.items()]) + 2
    y_max = max([y for y, unused in space[0].items()]) + 2
    z_max = max([z for z, unused in space[0][0].items()]) + 2
    w_max = max([w for w, unused in space[0][0][0].items()]) + 2

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            for z in range(z_min, z_max):
                for w in range(w_min, w_max):
                    current = get_state(x, y, z, w, space)

                    if current == "#":
                        set_state(x, y, z, w, apply_active(x, y, z, w, space), new_space)
                    elif current == ".":
                        set_state(x, y, z, w, apply_inactive(x, y, z, w, space), new_space)

    return new_space


def count_active(space):
    count = 0

    for key_x, value_x in space.items():
        for key_y, value_y in value_x.items():
            for key_z, value_z in value_y.items():
                for key_w, value_w in value_z.items():
                    if value_w == "#":
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
            set_state(x_pos, y_pos, 0, 0, char, space)
            y_pos += 1

        x_pos += 1

    for cycle in range(6):
        space = apply_cycle(space)

    result = count_active(space)
    print(f"There are {result} active cubes.")
