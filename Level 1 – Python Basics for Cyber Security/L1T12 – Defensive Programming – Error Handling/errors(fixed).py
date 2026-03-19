# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax error: Parentheses were missing, and print is a function, it requires parentheses to function
print("\n") # Syntax error: Parentheses were missing and indentation was fixed too.

# Variables declaring the user's age, casting the str to an int, and printing the result

age_Str = "24" #Runtimr error: Removed the "years old" part because int() function cannot change words or a text into integers/numbers.
#Syntax error: "==" double equal signs are used to compare not assign, if assign a variable only one equal "=" sign is used.
# Syntax error: Indentation was fixed too

age = int(age_Str) #syntax error: indentation was fixed
print("I'm" + str(age) + "years old.") #Runtime & syntax error: Python does not allow to concatenate a string and an integer unless you type Added str() and for the syntax error, it was indentation issues.

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 #Logical error & syntax error: The 3 is assigned as a string and not integer as in the next variable it is used in a calculation. And also, indentation issue was fixed too
total_years = age + years_from_now #syntax error: Indentation was fixed

print("The total number of years: " + str(total_years)) #Logical & Syntax error: Replaced string literal "answer_years" with the actual variable "total_years" and cast it to string).

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = (total_years + 0.5) * 12 # Logical error: "total" was not a defined variable, instead "total_years" should be used.
print("In 3 years and 6 months, I'll be " + str(int(total_months)) + " months old") #Runtime error: Cast total_months to str().

#HINT, 330 months is the correct answer

