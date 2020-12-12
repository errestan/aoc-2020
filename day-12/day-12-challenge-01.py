#!/usr/bin/env python3
""" Advent of Code: Day 12 Challenge 01."""


class Direction:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    RIGHT = "R"
    LEFT = "L"
    FORWARD = "F"


class Ship:
    @staticmethod
    def degrees_to_cardinal(degrees):
        cardinal = ""

        if degrees == 0:
            cardinal = Direction.NORTH
        elif degrees == 90:
            cardinal = Direction.EAST
        elif degrees == 180:
            cardinal = Direction.SOUTH
        elif degrees == 270:
            cardinal = Direction.WEST
        else:
            raise ValueError(f"Unknown direction {degrees}")

        return cardinal

    def __init__(self):
        self.possition = [0, 0]
        self.direction = 90

    def move(self, direction, distance):
        if direction == Direction.NORTH:
            self.possition[0] += distance
        elif direction == Direction.SOUTH:
            self.possition[0] -= distance
        elif direction == Direction.EAST:
            self.possition[1] += distance
        elif direction == Direction.WEST:
            self.possition[1] -= distance
        elif direction == Direction.FORWARD:
            self.move(Ship.degrees_to_cardinal(self.direction), distance)
        else:
            raise ValueError(f"Unknown movement {direction}")

    def turn(self, direction, distance):
        if direction == Direction.LEFT:
            self.direction -= distance
        elif direction == Direction.RIGHT:
            self.direction += distance

        if self.direction >= 360:
            self.direction -= 360
        elif self.direction < 0:
            self.direction += 360

    def execute(self, direction, distance):
        if direction in "NSEWF":
            self.move(direction, distance)
        elif direction in "RL":
            self.turn(direction, distance)
        else:
            raise ValueError(f"Unknown direction{direction}")

    def __repr__(self):
        return f"{self.possition[0]},{self.possition[1]} heading {Ship.degrees_to_cardinal(self.direction)}"


def parse_directions(inpu):
    directions = []

    for line in input:
        line = line.strip()

        dir = line[:1]
        num = int(line[1:])

        directions.append((dir, num))

    return directions


if __name__ == "__main__":
    input = ""

    with open("day-12.input", "r") as file:
        input = file.readlines()

    ship = Ship()
    directions = parse_directions(input)

    for direction in directions:
        ship.execute(direction[0], direction[1])
        print(f"{direction[0]}: {direction[1]} - {ship}")

    h_distance = ship.possition[0] if ship.possition[0] >= 0 else -1 * ship.possition[0]
    v_distance = ship.possition[1] if ship.possition[1] >= 0 else -1 * ship.possition[1]

    print(f"Distance: {h_distance + v_distance}")
