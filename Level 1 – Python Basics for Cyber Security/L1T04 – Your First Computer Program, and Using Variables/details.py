"""
Task 2: Pseudocode
Ask the user to enter their name
Store the name in a variable as a string data type
Ask the user to enter their age
Store the age in a variable as an integer data type
Ask the user to enter their house number
Store the house number in a variable as a string data type
Ask the user to enter their street name
Store the street name in a variable as a string data type

print This is "name". He/she is "age" years old and lives at house number "house number" on "street name".
"""
#Task 2:

name = input("Enter your name: ")
age = int(input("Enter your age: "))
house_number = int(input("Enter your House Number: "))
street_name = input("Enter your Street Name: ")

print(f"This is {name}. He/she is {age} years old and lives at house number {house_number} on {street_name}.")