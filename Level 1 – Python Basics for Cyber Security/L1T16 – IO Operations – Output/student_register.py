#Practical Task:

students_num = int(input("Enter number of students you are registering: "))

with open("reg_form.txt", "w") as file:

    file.write("Exam Venue Attendance Register\n")
    file.write("\n")

    for exam in range(students_num):
        iD_number = input(f"Enter iD Number for Student {exam+1}: ")

    file.write(f"Student iD: {iD_number} | Student Signature: ...........................\n")

print("Registration form 'reg_form' has been successfully created.")