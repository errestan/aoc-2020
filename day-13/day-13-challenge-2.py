#!/usr/bin/env python3
""" Advent of Code: Day 13 Challenge 02."""


if __name__ == "__main__":
    input = ""

    with open("day-13.input", "r") as file:
        input = file.readlines()

    bus_numbers = [bus.strip() for bus in input[1].split(",")]
    start_time = 100000000000000
    last_bus = int(bus_numbers[-1])
    offset = start_time % int(bus_numbers[0])
    result = 0

    buses = {}

    for i in range(0, len(bus_numbers)):
        if bus_numbers[i] != "x":
            buses[i] = int(bus_numbers[i])

    while not result:
        time = start_time + offset

        for bus_offset, bus in buses.items():
            # print(f"{time} - {bus_offset}: {bus} = {(time + bus_offset) % bus}: {last_match}")
            if (time + bus_offset) % bus != 0:
                break

            if bus == last_bus:
                result = time

        offset += int(bus_numbers[0])

    print(f"Result: {result}")
