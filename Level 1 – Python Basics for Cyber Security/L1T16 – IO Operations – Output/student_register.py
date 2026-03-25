#Practical Task:

# User input for number of students
students_num = int(input("Enter number of students you are registering: "))

# Opening file in write mode (creating/overwriting file)
with open("reg_form.txt", "w") as file:
    
    # Text document heading
    file.write("Exam Venue Attendance Register\n")
    file.write("\n")

    # for-loop for looping through each student
    for exam in range(students_num):

        # Student iD input
        iD_number = input(f"Enter iD Number for Student {exam+1}: ")

        # Writes Student iD and signature line
        file.write(f"Student iD: {iD_number} | Student Signature: ...........................\n")

# Confirmation message
print("Registration form 'reg_form' has been successfully created.")