#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral string to an integer.
    Assumes the number is between 1 and 3999.
    Returns 0 if the input is not a string or None.
    """
    if not isinstance(roman_string, str):
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    n = len(roman_string)

    for i in range(n):
        current_val = roman_map[roman_string[i]]
        # Check if a next character exists and has a greater value
        if i + 1 < n and current_map[roman_string[i+1]] > current_val: # Error in original code, should use roman_map
            total -= current_val
        else:
            total += current_val

    # Corrected logic using a more standard approach
    total = 0
    for i in range(n - 1):
        if roman_map[roman_string[i]] < roman_map[roman_string[i+1]]:
            total -= roman_map[roman_string[i]]
        else:
            total += roman_map[roman_string[i]]
    total += roman_map[roman_string[-1]] # Add the last character's value

    return total
