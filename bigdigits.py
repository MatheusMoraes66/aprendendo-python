#!/usr/bin/env python3

import sys

Zero = [
    "  ***  ",
    " *   * ",
    "*     *",
    "*     *",
    "*     *",
    " *   * ",
    "  ***  "
] 
One = [
    "     * ",
    "    ** ",
    "   * * ",
    "  *  * ",
    "     * ",
    "     * ",
    "     * "
]

Digits = [Zero, One]


try:
    digits = sys.argv[1]
    row = 0 
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row].replace("*", str(number)) + "  "
            column += 1
        print(line)
        row += 1
    pass
except IndexError:
    print("usage: bigdisgits.py <numbers>")
except ValueError as err:
    print(err, "in", digits)