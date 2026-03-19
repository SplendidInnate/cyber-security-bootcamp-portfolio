# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Syntax Error: Strings must always be enclosed with quotes.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# Logical error: The variables were placed in wrong place holders or curly braces because when the sentence is printed it will sound improper.
# Syntax error: The f-string is missing as it should be put first before the qoutes so that the curly braces can fucntion.

print(full_spec)
# Syntax error: print is a function and it requires parentheses to function and print out the variable or any other statement wirtten within the parentheses.

