#!/usr/bin/python3

# Practical Task L2T03:

import sys

def array_to_string(arr):
    """
    Converts a list of strings into a single concatenated string with spaces
    between each element.
    """
    return " ".join(arr)

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print()
    else:
        result = array_to_string(args)
        print(result)

