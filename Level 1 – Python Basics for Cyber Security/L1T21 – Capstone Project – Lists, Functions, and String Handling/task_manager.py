# Practical Task:

"""
This module is for managing users and tasks.

It allows the user to:
- register a new user
- add a task
- view all tasks
- view their own tasks
- edit or complete tasks
- generate reports
- display statistics

"""

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w", encoding="utf-8") as default_file:
        pass

with open("tasks.txt", 'r', encoding="utf-8") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [task for task in task_data if task != ""]

task_list = []
for task in task_data:
    current_task = {}

    # Split by semicolon and manually add each component
    task_components = task.split(";")
    current_task['username'] = task_components[0]
    current_task['title'] = task_components[1]
    current_task['description'] = task_components[2]
    current_task['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    current_task['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    current_task['completed'] = task_components[5] == "Yes"

    task_list.append(current_task)


#====Login Section====
# This code reads usernames and password from the user.txt file to
# allow a user to login.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w", encoding="utf-8") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r', encoding="utf-8") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Question 2: A helper function to save all tasks back into tasks.txt.
def save_tasks():
    """This function saves the current task list into tasks.txt."""
    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        task_lines = []

        for task in task_list:
            task_line = ";".join([
                task["username"],
                task["title"],
                task["description"],
                task["due_date"].strftime(DATETIME_STRING_FORMAT),
                task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task["completed"] else "No"
            ])
            task_lines.append(task_line)

        task_file.write("\n".join(task_lines))

# Question 2: Refactor the register-user code into a function called reg_user.
# Question 3: Prevent duplicate usernames and let the user try again.
def reg_user(): 
    """ 
    This function registers a new user and saves them to user.txt.
    """
    if current_user != "admin":
        print("Only the admin can register a new user.")
        return

    while True:
        new_username = input("New Username: ").strip()

        if new_username in username_password:
            print("That username already exists. Please enter a different username.")
            continue

        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        username_password[new_username] = new_password

        with open("user.txt", "w", encoding="utf-8") as out_file:
            user_lines = []
            for username, password in username_password.items():
                user_lines.append(f"{username};{password}")
            out_file.write("\n".join(user_lines))

        print("New user added")
        break

# Question 2: Refactor the add-task code into a function called add_task.
def add_task():
    """
    This function collects task information, validates the username and date,
    then saves the task into tasks.txt.
    """
    task_username = input("Name of person assigned to task: ").strip()

    if task_username not in username_password:
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ").strip()
    task_description = input("Description of Task: ").strip()

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ").strip()
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    current_date = date.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": current_date,
        "completed": False
    }

    task_list.append(new_task)
    save_tasks()
    print("Task successfully added.")

# Question 2: Refactor the view-all code into a function called view_all.
def view_all():
    """This function displays all tasks in a user-friendly format."""
    if len(task_list) == 0:
        print("There are no tasks available.")
        return

    for task in task_list:
        display = (
            "_____________________________________________________________\n"
            f"Task:               {task['title']}\n"
            f"Assigned to:        {task['username']}\n"
            f"Date Assigned:      {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            f"Due Date:           {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            f"Task Complete?      {'Yes' if task['completed'] else 'No'}\n"
            "Task Description:\n"
            f"{task['description']}\n"
            "_____________________________________________________________"
        )
        print(display)

# Question 4: Create the view_mine function.
def view_mine():
    """This function is for viewing and editing my tasks."""
    user_task_indexes = []

    for index, task in enumerate(task_list, start=1):
        if task["username"] == current_user:
            user_task_indexes.append(index)

            display = (
                "_____________________________________________________________\n"
                f"Task Number:        {index}\n"
                f"Task:               {task['title']}\n"
                f"Assigned to:        {task['username']}\n"
                f"Date Assigned:      {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                f"Due Date:           {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                f"Task Complete?      {'Yes' if task['completed'] else 'No'}\n"
                "Task Description:\n"
                f"{task['description']}\n"
                "_____________________________________________________________"
            )
            print(display)

    if len(user_task_indexes) == 0:
        print("You have no tasks assigned to you.")
        return

    while True:
        try:
            task_choice = int(input("Enter a task number to select it or -1 to return: "))

            if task_choice == -1:
                return

            if task_choice not in user_task_indexes:
                print("Invalid task number. Please select one of your task numbers.")
                continue

            selected_task = task_list[task_choice - 1]

            action = input(
                "Enter 'c' to mark complete or 'e' to edit the task: "
            ).lower()

            if action == "c":
                selected_task["completed"] = True
                save_tasks()
                print("Task marked as complete.")
                return

            elif action == "e":
                if selected_task["completed"]:
                    print("This task has already been completed and cannot be edited.")
                    return

                edit_option = input("Enter 'u' to edit username or 'd' to edit due date: ").lower()

                if edit_option == "u":
                    new_username = input("Enter the new username: ").strip()

                    if new_username not in username_password:
                        print("User does not exist. Task not updated.")
                        return

                    selected_task["username"] = new_username
                    save_tasks()
                    print("Username updated successfully.")
                    return

                elif edit_option == "d":
                    while True:
                        try:
                            new_due_date = input("Enter the new due date (YYYY-MM-DD): ").strip()
                            new_due_date = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            selected_task["due_date"] = new_due_date
                            save_tasks()
                            print("Due date updated successfully.")
                            return
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")

                else:
                    print("Invalid edit option.")
                    continue

            else:
                print("Invalid option selected.")
        except ValueError:
            print("Please enter a valid number.")

# Question 5 and 6: Created the generate_reports() function and added report generation logic.
def generate_reports():
    """This function creates task_overview.txt and user_overview.txt"""
    total_tasks = len(task_list)
    total_completed = 0
    total_incomplete = 0
    total_overdue = 0
    today = date.today()

    for task in task_list:
        if task["completed"]:
            total_completed += 1
        else:
            total_incomplete += 1
            if task["due_date"].date() < today:
                total_overdue += 1

    percentage_incomplete = 0
    percentage_overdue = 0

    if total_tasks > 0:
        percentage_incomplete = (total_incomplete / total_tasks) * 100
        percentage_overdue = (total_overdue / total_tasks) * 100

    with open("task_overview.txt", "w", encoding="utf-8") as task_overview:
        task_overview.write("Task Overview\n")
        task_overview.write("_____________________________________________________________\n")
        task_overview.write(f"Total number of tasks: {total_tasks}\n")
        task_overview.write(f"Total number of completed tasks: {total_completed}\n")
        task_overview.write(f"Total number of uncompleted tasks: {total_incomplete}\n")
        task_overview.write(f"Total number of overdue tasks: {total_overdue}\n")
        task_overview.write(f"Percentage of incomplete tasks: {percentage_incomplete:.0f}%\n")
        task_overview.write(f"Percentage of overdue tasks: {percentage_overdue:.0f}%\n")

    total_users = len(username_password)

    with open("user_overview.txt", "w", encoding="utf-8") as user_overview:
        user_overview.write("User Overview\n")
        user_overview.write("_____________________________________________________________\n")
        user_overview.write(f"Total number of users: {total_users}\n")
        user_overview.write(f"Total number of tasks: {total_tasks}\n")

        for username in username_password:
            user_total_tasks = 0
            user_completed_tasks = 0
            user_incomplete_tasks = 0
            user_overdue_tasks = 0

            for task in task_list:
                if task["username"] == username:
                    user_total_tasks += 1

                    if task["completed"]:
                        user_completed_tasks += 1
                    else:
                        user_incomplete_tasks += 1
                        if task["due_date"].date() < today:
                            user_overdue_tasks += 1

            percentage_user_assigned = 0
            percentage_user_completed = 0
            percentage_user_incomplete = 0
            percentage_user_overdue = 0

            if total_tasks > 0:
                percentage_user_assigned = (user_total_tasks / total_tasks) * 100

            if user_total_tasks > 0:
                percentage_user_completed = (user_completed_tasks / user_total_tasks) * 100
                percentage_user_incomplete = (user_incomplete_tasks / user_total_tasks) * 100
                percentage_user_overdue = (user_overdue_tasks / user_total_tasks) * 100

            user_overview.write("\n")
            user_overview.write(f"Username: {username}\n")
            user_overview.write(f"Total tasks assigned to user: {user_total_tasks}\n")
            user_overview.write(f"Percentage of total tasks assigned to user: {percentage_user_assigned:.0f}%\n")
            user_overview.write(f"Percentage of tasks completed by user: {percentage_user_completed:.0f}%\n")
            user_overview.write(f"Percentage of tasks still incomplete for user: {percentage_user_incomplete:.0f}%\n")
            user_overview.write(f"Percentage of tasks overdue for user: {percentage_user_overdue:.0f}%\n")

while True:
    print("LOGIN")
    current_user = input("Username: ")
    current_pass = input("Password: ")
    if current_user not in username_password:
        print("User does not exist")
        continue
    if username_password[current_user] != current_pass:
        print("Wrong password")
        continue
    print("Login Successful!")
    break

# Question 7: Displaying statistics
def display_statistics():
    """This function is for displaying statistics in a user-friendly format."""
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()

    print("\n================ TASK STATISTICS ================\n")
    with open("task_overview.txt", "r", encoding="utf-8") as task_overview:
        for line in task_overview:
            print(line.strip())

    print("\n================ USER STATISTICS ================\n")
    with open("user_overview.txt", "r", encoding="utf-8") as user_overview:
        for line in user_overview:
            print(line.strip())

    print("\n================================================\n")

#====Main Menu Section====
while True:

    # Question 5: Menu for the admin.
    if current_user == "admin":

    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
        print()
        menu = input("Select one of the following Options below:\n"
                 "r - Registering a user\n"
                 "a - Adding a task\n"
                 "va - View all tasks\n"
                 "vm - View my task\n"
                 "gr - Generate reports\n" 
                 "ds - Display statistics\n"
                 "e - Exit\n"
                 ": ").lower()
    
    else:
        print()
        menu = input(
            "Select one of the following Options below:\n"
            "a - Adding a task\n"
            "va - View all tasks\n"
            "vm - View my task\n"
            "e - Exit\n"
            ": "
        ).lower()

    # Add a new user to the user.txt file
    if menu == "r":
        reg_user() # Call the reg_user() function
       
    # Question 2: Call the add-task() function.
    elif menu == "a":
        add_task()
    
    # Question 2: Call the view-all() function.
    elif menu == "va":
        view_all()

    # Question 4: Call the view-mine() function.
    elif menu == "vm":
        view_mine()

    # Question 5 and 6: Adding the menu option to generate reports.
    elif menu == "gr":
        if current_user == "admin":
            generate_reports()
            print("Reports generated successfully.")
        else:
            print("Only the admin can generate reports.")

    # Question 7: Displaying statistics by reading from the generated report files.
    # If the files do not exist, they will be generated first.
    elif menu == "ds":
        if current_user == "admin":
            display_statistics()
        else:
            print("Only the admin can display statistics.")

    elif menu == "e":
        print("Goodbye!!!")
        break

    else:
        print("You have made a wrong choice, Please Try again")
