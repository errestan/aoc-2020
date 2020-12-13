#!/usr/bin/env python3
""" Advent of Code: Day 13 Challenge 01."""


if __name__ == "__main__":
    input = ""

    with open("day-13.input", "r") as file:
        input = file.readlines()

    arrival_time = int(input[0].strip())
    bus_numbers = [int(bus.strip()) for bus in input[1].split(",") if bus != "x"]
    bus_numbers.sort()

    bus_timetable = {}

    for bus in bus_numbers:
        id = bus
        times = []

        for time in range(0, arrival_time + bus, bus):
            times.append(time)

        bus_timetable[bus] = times

    results = ()

    print(f"Checking buses between: {arrival_time} and {arrival_time + bus_numbers[-1]}")

    for time in range(arrival_time, arrival_time + bus_numbers[-1]):
        for bus, times in bus_timetable.items():
            if time in times:
                diff = time - arrival_time
                results = (bus, time, diff)
                break

        if results:
            break

    print(f"{results}")
    print(f"{results[0] * results[2]}")
