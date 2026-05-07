#!/usr/bin/python3

# Practical Task L2TO3:

import sys

def std_in():
    """
    This function reads input from standard input (stdin) and prints each line
    to standard output (stdout).
    """
    for line in sys.stdin:
        print(line, end=" ")

def infile(file):
    """
    This function reads from the specified file and handle the case where it doesn't exist
    """
    try:
        with open(file, "r") as f:
            for line in f:
                print(line, end=" ")
    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile(sys.argv[1])
    else:
        std_in()
        