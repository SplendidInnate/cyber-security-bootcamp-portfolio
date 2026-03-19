# Optional Challenge Program with Different Errors
# A simple grade calculator with errors

# Get student info
student_name = input("Enter your Name: )
# (compilation) Syntax error: Missing quote!
print(f"Student: {student_name}")

# Get test scores
test1 = int(input("Enter score for test 1: "))
test2 = int(input("Enter score for test 2: "))
test3 = int(input("Enter score for test 3: "))

# (compilation)) Syntax error 2: A missing colon(:).
if test1 > test2  # Missing colon here
    print("Test 1 score is higher than test 2")

# Runtime error 1: Division by zero
print("Calculating Average")
total_points = 100
# Runtime error: Can't divide by zero if total_points is 0
average = (test1 + test2 + test3) / 0  #Runtime error
print(f"Average: {average}")

# Runtime error 2: Index error
grades = ["Excellent", "Congratulations", "Good Work", "Fail"]
print(f"First grade: {grades[0]}")
print(f"Last grade: {grades[10]}")  #Runtime error: index 10 doesn't exist!

# Logical error: Wrong grade calculation
print("Final Grade:")
total = test1 + test2 + test3

# Logical error: Wrong grade boundaries
if total > 90:  # Should be >= 90 for an excellent
    letter_grade = "Excellent"
elif total > 80:  # Should be >= 80 for a congratulations
    letter_grade = "Congratulations"
elif total > 70:  # Should be >= 70 for a good work
    letter_grade = "Good work"
else:
    letter_grade = "Fail. Do better next time"

print(f"Total score: {total}")
print(f"Letter grade: {letter_grade}")
print("A score of 90 should be an excellent, but gets a congratulations in this program!")