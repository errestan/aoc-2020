#!/usr/bin/env python3
""" Advent of Code: Day 20 Challenge 02."""


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


class Image:
    def __init__(self):
        pass


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


def find_neighbour(first, second, tiles):
    for tile in tiles:
        count = 0
        value = 0

        if first:
            count += compare_edges(first, tile)
            value += 1

        if second:
            count += compare_edges(second, tile)
            value += 1

        if count == value:
            return tile

    return None


def is_edge(x, y, x_max, y_max):
    if (
        (x == 0 and y > 0 and y < y_max)
        or (x == x_max and y > 0 and y < y_max)
        or (y == 0 and x > 0 and x < x_max)
        or (y == y_max and x > 0 and x < x_max)
    ):
        return True

    return False


def is_corner(x, y, x_max, y_max):
    if (x == 0 and y == 0) or (x == 0 and y == y_max) or (x == x_max and y == 0) or (x == x_max and y == y_max):
        return True

    return False


def print_image(image):
    x_max = len(image[0])
    y_max = len(image[0])

    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if image[x][y]:
                print(image[x][y].id, end=", ")
            else:
                print("????", end=", ")
        print()


def assemble_image(corners, edges, others):
    length = 2 + int((len(edges) / 4))
    x_max = length - 1
    y_max = length - 1

    image = {}
    image[0] = {0: corners[0]}

    for x in range(length):
        for y in range(length):
            next = None

            if x == 0 and y == 0:
                next = image[x][y]

            above = None
            left = None

            if y > 0:
                above = image[x][y - 1]

            if x > 0:
                left = image[x - 1][y]

            tiles = None

            if is_edge(x, y, x_max, y_max):
                tiles = edges
            elif is_corner(x, y, x_max, y_max):
                tiles = corners
            else:
                tiles = others

            if not next and (above or left):
                next = find_neighbour(above, left, tiles)

            if not image.get(x):
                image[x] = {}

            # print(f"{x},{y} {next.id if next else next} {len(tiles)}")
            image[x][y] = next
            if next in tiles:
                # print(f"Removing tile {next.id}")
                tiles.remove(next)

    return image


if __name__ == "__main__":
    input = ""

    with open("day-20.test", "r") as file:
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
    centres = []
    edges = []

    for first in tiles:
        count = 0

        for second in tiles:
            if first.id == second.id:
                continue

            count += compare_edges(first, second)

        if count == 2:
            corners.append(first)
        elif count == 3:
            edges.append(first)
        elif count == 4:
            centres.append(first)

    print(f"Corners {len(corners)}, edges {len(edges)} and other {len(centres)}")

    image = assemble_image(corners, edges, centres)
