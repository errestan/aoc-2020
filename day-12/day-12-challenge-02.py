#!/usr/bin/env python3
""" Advent of Code: Day 12 Challenge 02."""

import math


class Direction:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    RIGHT = "R"
    LEFT = "L"
    FORWARD = "F"


class Ship:
    def __init__(self):
        self.position = [0, 0]
        self.waypoint = [10, 1]

    def move(self, distance):
        self.position[0] += self.waypoint[0] * distance
        self.position[1] += self.waypoint[1] * distance

    def move_waypoint(self, direction, distance):
        if direction == Direction.NORTH:
            self.waypoint[1] += distance
        elif direction == Direction.SOUTH:
            self.waypoint[1] -= distance
        elif direction == Direction.EAST:
            self.waypoint[0] += distance
        elif direction == Direction.WEST:
            self.waypoint[0] -= distance
        else:
            raise ValueError(f"Unknown movement {direction}")

    def turn(self, direction, distance):
        angle_degrees = distance if direction == Direction.LEFT else 360 - distance
        angle_radians = math.radians(angle_degrees)

        new_x = int(int(self.waypoint[0] * math.cos(angle_radians)) - int(self.waypoint[1] * math.sin(angle_radians)))
        new_y = int(int(self.waypoint[1] * math.cos(angle_radians)) + int(self.waypoint[0] * math.sin(angle_radians)))

        self.waypoint[0] = new_x
        self.waypoint[1] = new_y

    def execute(self, direction, distance):
        if direction in "NSEW":
            self.move_waypoint(direction, distance)
        elif direction in "RL":
            self.turn(direction, distance)
        elif direction == "F":
            self.move(distance)
        else:
            raise ValueError(f"Unknown direction{direction}")

    def __repr__(self):
        return f"{self.position[0]},{self.position[1]} Waypoint {self.waypoint[0]},{self.waypoint[1]}"


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

    h_distance = ship.position[0] if ship.position[0] >= 0 else -1 * ship.position[0]
    v_distance = ship.position[1] if ship.position[1] >= 0 else -1 * ship.position[1]

    print(f"Distance: {h_distance + v_distance}")
