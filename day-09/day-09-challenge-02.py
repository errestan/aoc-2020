#!/usr/bin/env python3
""" Advent of Code: Day 08 Challenge 02."""


def is_sum_of(sum, start, end, data):
    for i in range(start, end):
        for j in range(start, end):
            if i == j:
                continue

            if data[i] + data[j] == sum:
                return True

    return False


def find_weakness(sum, data):
    result = 0

    for i in range(0, len(data)):
        total = data[i]
        j = i + 1

        for j in range(i + 1, len(data)):
            total += data[j]

            if total < sum:
                continue
            else:
                break

        if total == sum:
            result_list = data[i:j]
            result_list.sort()
            result = result_list[0] + result_list[-1]
            break

    return result


if __name__ == "__main__":
    input = ""

    with open("day-09-challenge-02.input", "r") as file:
        input = file.readlines()

    preamble_len = 25

    stream = [int(number) for number in input]
    length = len(stream)

    sum = 0
    i = 0

    try:
        for i in range(25, length - 1):
            sum = stream[i]
            min = i - preamble_len
            max = i

            if not is_sum_of(sum, min, max, stream):
                raise ValueError(f"{sum} is not the of any of the previous {preamble_len} numbers.")
    except ValueError as e:
        print(e)
        print(f"Checking number from index 0 to {i}")
        weakness = find_weakness(sum, stream[:i])
        print(f"Weakness is {weakness}")
