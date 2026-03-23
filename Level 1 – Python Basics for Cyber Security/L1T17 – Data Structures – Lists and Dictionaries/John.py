#Auto-Grade Task 1:

incorrect_names = []

names = input("Enter names: ")

while names.lower() != "john":
    incorrect_names.append(names)
    names = input("Enter names: ")

print(" ")
print(f"Incorrect names: {incorrect_names}")