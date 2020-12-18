#!/usr/bin/env python3
""" Advent of Code: Day 18 Challenge 02."""


def evaluate(pos, expression):
    res = 0
    op = "+"

    while pos < len(expression):
        part = expression[pos]
        # print(f"[{pos}]: {part}")

        if part.isnumeric():
            val = int(part)

            # print(f"{res} {op} {val}")
            res = res + val if op == "+" else res * val
        elif part == "+" or part == "*":
            op = part
            if op == "*":
                pos, val = evaluate(pos + 1, expression)
                # print(f"{res} {op} {val}")
                res = res + val if op == "+" else res * val
                break
        elif part == "(":
            pos, val = evaluate(pos + 1, expression)
            # print(f"{res} {op} {val}")
            res = res + val if op == "+" else res * val
        elif part == ")":
            break
        elif part == "":
            pos += 1
            continue
        else:
            raise ValueError(f"Unknown part '{part}'")

        pos += 1

    # print(f"= {res}")
    return (pos, res)


def evaluate_string(expression_text):
    expression = expression_text.split(" ")
    return evaluate(0, expression)[1]


if __name__ == "__main__":
    input = ""

    with open("day-18.input", "r") as file:
        input = file.readlines()

    results = []

    for line in input:
        line = line.strip()
        line = line.replace("(", "( ")
        line = line.replace(")", " )")

        results.append(evaluate_string(line))

    total = sum(results)
    print(f"The total is: {total}")
