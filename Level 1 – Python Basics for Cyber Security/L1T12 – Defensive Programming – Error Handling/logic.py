# Program with a logical error

# This program is supposed to calculate the average of three test scores
# but contains a logical error in the calculation

# Get test scores from user
test_1 = float(input("Enter score for test 1: "))
test_2 = float(input("Enter score for test 2: "))
test_3 = float(input("Enter score for test 3: "))

# Calculate average - Logical error is don here.
# The 3 test scores were added but forgot to divide by 3.
average = test_1 + test_2 + test_3  # Logical error: missing division by 3

# Display the result
print(f"Your average score is: {average}")