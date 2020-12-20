#!/usr/bin/env python3
""" Advent of Code: Day 20 Challenge 01."""

import numpy


class Tile:
    def __init__(self, id, data):
        self.id = int(id)
        self.data = []

        for line in data:
            line = line.strip()

            row = []

            for char in line:
                char = char.strip()
                row.append(char)

            self.data.append(row)

    def top(self):
        return "".join(self.data[0])

    def topr(self):
        return "".join([self.data[0][x - 1] for x in range(len(self.data[0]), 0, -1)])

    def bottom(self):
        return "".join([self.data[-1][x] for x in range(len(self.data[-1]))])

    def bottomr(self):
        return "".join([self.data[-1][x - 1] for x in range(len(self.data[-1]), 0, -1)])

    def left(self):
        return "".join([self.data[y][0] for y in range(len(self.data))])

    def leftr(self):
        return "".join([self.data[y - 1][0] for y in range(len(self.data), 0, -1)])

    def right(self):
        return "".join([self.data[y][-1] for y in range(len(self.data))])

    def rightr(self):
        return "".join([self.data[y - 1][-1] for y in range(len(self.data), 0, -1)])

    def __repr__(self):
        output = []

        for row in self.data:
            line = []
            for cell in row:
                line.append(cell)
            output.append("".join(line))

        return "\n".join(output)


def compare_edges(first, second):
    # print(f"Comparing {first.id} {second.id}")
    first_edges = []
    second_edges = []

    first_edges.append(first.top())
    first_edges.append(first.bottom())
    first_edges.append(first.left())
    first_edges.append(first.right())

    second_edges.append(second.top())
    second_edges.append(second.topr())

    second_edges.append(second.bottom())
    second_edges.append(second.bottomr())

    second_edges.append(second.left())
    second_edges.append(second.leftr())

    second_edges.append(second.right())
    second_edges.append(second.rightr())

    count = 0

    for first_edge in first_edges:
        for second_edge in second_edges:
            # print(f"{first_edge} {second_edge}")
            if first_edge == second_edge:
                count += 1

    # print(f"Count: {count}")
    return count


if __name__ == "__main__":
    input = ""

    with open("day-20.input", "r") as file:
        input = file.readlines()

    tile_id = 0
    tiles = []
    data = []

    for i in range(len(input)):
        line = input[i].strip()

        if line.startswith("Tile"):
            tile_id = line.split(" ")[1].rstrip(":")
        elif len(line) == 0:
            tiles.append(Tile(tile_id, data))

            tile_id = 0
            data = []
        else:
            data.append(line)

    corners = []

    for first in tiles:
        count = 0

        for second in tiles:
            if first.id == second.id:
                continue

            count += compare_edges(first, second)

        if count == 2:
            corners.append(first)

    corner_ids = [int(tile.id) for tile in corners]
    total = numpy.prod(corner_ids)
    print(corner_ids)
    print(total)
