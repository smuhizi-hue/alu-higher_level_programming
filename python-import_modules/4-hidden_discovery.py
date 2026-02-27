#!/usr/bin/python3
# Assuming hidden_4.pyc is in the same directory
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    all_names = dir(hidden_4)

    # Filter out names that start with '_' and sort them alphabetically
    public_names = sorted([name for name in all_names if not name.startswith('_')])

    # Print each name on a new line
    for name in public_names:
        print(name)
