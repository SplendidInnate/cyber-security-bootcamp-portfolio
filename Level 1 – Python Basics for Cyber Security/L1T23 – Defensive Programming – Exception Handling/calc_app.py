# Practical Task L1T23:

def calculate():
    """
    This function takes two numbers and an operator, calculates
    and then saves the results to equations.txt
    """
    try: # Try-except error handle
        num_1 = float(input("Enter the first number: ")) # First number input
        operator = input("Enter the operator (+, -, *, /): ") # Operator sign input
        num_2 = float(input("Enter the second number: ")) # Second number input

        if operator == "+":
            answer = num_1 + num_2
        
        elif operator == "-":
            answer = num_1 - num_2

        elif operator == "*":
            answer = num_1 * num_2

        elif operator == "/":
            if num_2 == 0:
                print("Cannot divide by zero")
                return
            answer = num_1 / num_2
        
        else:
            print("Invalid Operator Entered.")
            return
        
        equation = f"{num_1} {operator} {num_2} = {answer:.2f}" # Equation format
        print(equation) # Equation display

        with open("equations.txt", "a") as file:
            file.write(equation + "\n") # Save equation

    except ValueError: # except error handle
        print("Invalid number input.")

def previous_equations():
    """
    This function prints previous equations from equations.txt
    and handles the case where the file does not exist. 
    """
    try:
        with open("equations.txt", "r") as file:
            equations = file.read()

            if equations:
                print("\n========== Previous Calculations ==========")
                print(equations)
            else:
                print("No Calculations")

    except FileNotFoundError:
        print("No previous calculations were done/found.")

# Menu option
print("=============== Main Menu ===============")

try:
    option = int(input("Enter '1' to Calculate, OR, Enter '2' to print previous calculations: "))
    
    if option == 1:
        calculate() # Option 1 for perfoming calculations

    elif option == 2:
        previous_equations() # Option 2 to print previous calculations

    else:
        print("Invalid Option.")

except ValueError:
    print("Invalid Option")