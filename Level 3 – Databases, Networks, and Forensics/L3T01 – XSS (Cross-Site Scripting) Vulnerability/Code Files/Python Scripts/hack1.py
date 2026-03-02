"""
This script evaluates mathematical expressions in the form 'number1
operator number2'.The expression can be read from a file named 'hack1.txt'
or input manually by the user.Supported operators are '+', '-', '*', and '/'.

If 'hack1.txt' is present in the same directory, the script will read the
expression from this file.If the file does not exist, it will prompt the user
to enter the expression manually.
"""

import os
from vulnerability import hack

print("This code will evaluate sums of the form 'number1 operator number2'")

# Check if the 'hack1.txt' file exists. If it does, read input from the file.
if os.path.exists("hack1.txt"):
    with open("hack1.txt", 'r', encoding='utf-8') as in_file:
        user_input = in_file.read()
# Otherwise, prompt the user to enter the expression manually.
else:
    user_input = input("Enter your sum\n: ")

# Split the user input into components and validate the format.
user_sum = user_input.split(" ")
if len(user_sum) != 3:
    print("Please enter a valid sum, with a space between each number\
          and operator.")
else:
    print(eval(" ".join(user_sum)))
