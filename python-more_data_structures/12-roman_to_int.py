#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer.

    Return 0 if roman_string is not a string or is None.
    """
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_string = roman_string.upper()
    if roman_string == "":
        return 0

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    total = 0
    prev = 0

    for ch in reversed(roman_string):
        val = values.get(ch)
        if val is None:
            return 0
        if val < prev:
            total -= val
        else:
            total += val
            prev = val

    return total
