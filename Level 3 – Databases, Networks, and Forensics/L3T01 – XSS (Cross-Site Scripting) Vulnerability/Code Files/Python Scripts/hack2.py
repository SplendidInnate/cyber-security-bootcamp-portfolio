"""
This script reads a number from a file named 'hack2.txt' or from user input,
and adds 1 to it.The script uses `eval` to evaluate the expression, which can
execute arbitrary code manipulated.

If 'hack2.txt' is present in the same directory, the script
will read the number from this file.If the file does not exist, it will prompt
the user to enter the number manually.
The result of the addition is then printed to the console.
"""

import os
from vulnerability import hack

print("This code reads in a number and adds 1 to it")

# If the 'hack2.txt' file exists, read the number from the file.
if os.path.exists("hack2.txt"):
    with open("hack2.txt", 'r', encoding='utf-8') as in_file:
        user_input = in_file.read()
# Otherwise, prompt the user to enter the number manually.
else:
    user_input = input("Enter your number\n: ")

# Then, we run the code
print(eval(f'{user_input} + 1'))