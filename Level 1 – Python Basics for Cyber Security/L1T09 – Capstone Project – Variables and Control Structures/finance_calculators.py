#Practical Task: Capstone Project
import math

#User option display
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
print(" ")

#user input option
option = input("Enter either ''investment'' or ''bond'' from the Menu above to proceed: ")
option = option.lower()
#Converts user input to lowercase so capitalisation doesn't matter

#if statement operation if user enters "investment"
if option == "investment":
    amount = float(input("How much would you like to deposit: R"))
    interest_rate = float(input("At what interest rate (Please enter only the number): "))/100
    years = int(input("Enter the number of years you plan to invest: "))
    print("Would you like to invest in a ''simple'' or ''compound interest'': ")
    interest = input()
    interest = interest.lower()

#nested if-statemnet if user selects "simple" or "compound" interest option
    if interest == "simple": #simple
        
        simple_interest = amount*(1+interest_rate*years)
        print(" ")

        #Displaying output
        print(f"Your investment amount after {years} years in simple interest will be: R{simple_interest:.2f}")
        print("Thank You.")

    if interest == "compound": #compound
        compound_interest = amount*math.pow((1+interest_rate),years)
        print(" ")

        #displaying output
        print(f"Your investment amount after {years} years in compound interest will be: R{compound_interest:.2f}")
        print("Thank You.")

#elif statement operation for "bond" option
elif option == "bond":
    value = float(input("Please enter the Present Value of the House: R"))
    interest_rate = float(input("Please enter the Interest Rate (only the integer): "))
    months_repayment = float(input("Please enter the Number of Months you would take to repay the bond: "))
    repayment = ((interest_rate/100)/12*value)/(1-(1+(interest_rate/100)/12)**(-months_repayment))
    print(" ")

    #Displaying output
    print(f"The monthly amount paid will be: R{repayment:.2f}")
    print("Thank You.")

#Incase the user enters something else, an error messaage will pop-up and acknowledge the user
else:
    print("Error!! Please enter 'Bond' OR 'Investment'.")
    print("Thank You.")
    
    