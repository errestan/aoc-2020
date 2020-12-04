#!/usr/bin/enve python3
""" Advent of Code 2020: Day 04 Challenge 02."""


class Passport:
    @staticmethod
    def from_dictionary(data):
        return Passport(
            data["byr"], data["iyr"], data["eyr"], data["hgt"], data["hcl"], data["ecl"], data["pid"], data.get("cid")
        )

    @staticmethod
    def _validate_date(date, start, end):
        if len(date) != 4:
            raise ValueError

        if int(date) < start or int(date) > end:
            raise ValueError

        return date

    def _set_byr(self, byr):
        self.byr = Passport._validate_date(byr, 1920, 2002)

    def _set_iyr(self, iyr):
        self.iyr = Passport._validate_date(iyr, 2010, 2020)

    def _set_eyr(self, eyr):
        self.eyr = Passport._validate_date(eyr, 2020, 2030)

    def _set_hgt(self, hgt):
        if "cm" in hgt:
            value = int(hgt.rstrip("cm"))

            if value < 150 or value > 198:
                raise ValueError
        elif "in" in hgt:
            value = int(hgt.rstrip("in"))

            if value < 59 or value > 76:
                raise ValueError
        else:
            raise ValueError(f"Invalid hight: {hgt}")

        self.hgt = hgt

    def _set_hcl(self, hcl):
        if len(hcl) != 7:
            raise ValueError(hcl)

        value = int(hcl.lstrip("#"), 16)

        self.hcl = hcl

    def _set_ecl(self, ecl):
        eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if len(ecl) != 3:
            raise ValueError(ecl)

        if ecl not in eye_colours:
            raise ValueError(ecl)

        self.ecl = ecl

    def _set_pid(self, pid):
        if len(pid) != 9:
            raise ValueError(pid)

        value = int(pid)

        self.pid = pid

    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=""):
        self._set_byr(byr)
        self._set_iyr(iyr)
        self._set_eyr(eyr)

        self._set_hgt(hgt)
        self._set_hcl(hcl)
        self._set_ecl(ecl)

        self._set_pid(pid)

        self.cid = cid


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_valid(fields):
    for field in required_fields:
        if field not in fields:
            return False

    return True


def parse_passport(lines):
    fields = {}

    for line in lines:
        line = line.strip()

        pairs = line.split(" ")

        for pair in pairs:
            key, value = pair.split(":")
            fields[key] = value

    return fields


if __name__ == "__main__":
    input = ""

    with open("day-04-challenge-01.input", "r") as file:
        input = file.readlines()

    entries = []
    lines = []
    total = 0

    for line in input:
        line = line.strip()

        if line == "":
            total = total + 1
            entries.append(lines)
            lines = []
            continue

        lines.append(line)

    passports = []

    for lines in entries:
        fields = parse_passport(lines)

        if is_valid(fields):
            try:
                passport = Passport.from_dictionary(fields)

                passports.append(passport)
            except ValueError:
                print("Skipping invalid passport")

    count = len(passports)

    print(f"There are {count} valid passports out of {total}")
