#!/usr/bin/python3

# Practical Task L2TO3:

import sys

def match(source, needle):
    """
    Searches for a specified 'needle' string within a list of 'source' strings.
    """
    for line in source:
        if needle in line:
            print(line, end=" ")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        needle = sys.argv[1]
        match(sys.stdin, needle)
    elif len(sys.argv) == 3:
        needle = sys.argv[1]
        filename = sys.argv[2]
        try:
            with open(filename, "r") as f:
                match(f, needle)
        except FileNotFoundError:
            print(f"Error: file {filename} not found.")
            
