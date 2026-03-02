import os
from vulnerability import hack
# This is an example of how we will be injecting code

# First, we check if the .txt file exists. If so, we get input from the file
if os.path.exists("example.txt"):
    with open("example.txt", 'r') as in_file:
        user_input = in_file.read()
# Otherwise, we get it from the command line
else:
    user_input = input("What code would you like to run?\n:")

# Then, we run the code
print(eval(user_input))