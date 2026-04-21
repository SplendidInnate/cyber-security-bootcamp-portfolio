"""
Practical Task L1T24:

Email simulator program

"""
# --- OOP Email Simulator --- #

# --- Email Class --- #
# Class, constructor and methods to create a new Email object.

class Email():
    """ This class is for creating email objects."""
    def __init__(self, email_address, Subject_line, email_content):
        """ This constructor is for setting up the email details."""
# Initialise the instance variables for each email.
        self.email_address = email_address
        self.Subject_line = Subject_line
        self.email_content = email_content
        self.has_been_read = False

# Mark_as_read() method to change the 'has_been_read'
    def mark_as_read(self):
        """ This function is for marking an email as read."""
# instance variable for a specific object from False to True.
        self.has_been_read = True

# --- Lists --- #
# An empty list outside the class to store the email objects.
inbox = []

# --- Functions --- #

def populate_inbox():
    """ This function is for creating sample emails and add them to the inbox."""

    email_1 = Email(
        "Welcome@HyperionDev.com",
        "Welcome to HyperionDev!",
        "Thank you for joining HyperionDev Bootcamp, We are excited to have you."
                   )
    
    email_2 = Email(
        "bootcamp@hyperiondev.com",
        "Great work on the bootcamp!",
        "You are doing a great job. Keep working hard and stay focused."
                   )
    
    email_3 = Email(
        "results@hyperiondev.com",
        "Excellent Marks!",
        "Congratulation on your outstanding perfomance in the bootcamp!"
                   )
    
    # Add the emails to the Inbox list
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)

def list_emails():
    """This function is for listing all email subject lines with index numbers."""
    if len(inbox) == 0:
        print("\nYour inbox is empty.\n")
    else:
        print("\nInbox: ")

        # Print each subject line with its index
        for index, email in enumerate(inbox):
            print(f"{index}: {email.Subject_line}")
            print()

def read_email(index):
    """ This email is for displaying a selected email and marking it as read."""
    # Check if index is valid
    if 0 <= index < len(inbox):
        email = inbox[index]

        # Display the full email details
        print("\nEmail Details: ")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.Subject_line}")
        print(f"Content: {email.email_content}\n")
        
        # Mark email as read
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        print("\nInvalid Email Index.\n")

def view_unread_emails():
    """ This function is for displaying unread email subject lines only. """
    # Keep track of whether unread emails exist
    unread_found = False

    print("\nUnread Emails: ")
    # For-loop to loop through emails and display unread emails only
    for index, email in enumerate(inbox):
        if email.has_been_read is False:
            print(f"{index} {email.Subject_line}")
            unread_found = True

    if unread_found is False:
        print("There are no unread emails.")
    print()

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Display the menu options for each iteration of the loop.
while True:
    try:
        user_choice = int(
            input(
                """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
            )
        )

        if user_choice == 1:
            # I first list all emails before asking which one to read
            list_emails()

            try:
                index = int(input("Enter the index of the email you would like to read: "))
                read_email(index)
            except ValueError:
                print("\nPlease enter a valid number for the email index.\n")

        elif user_choice == 2:
            # Displaying only unread emails
            view_unread_emails()

        elif user_choice == 3:
            # End the program
            print("\nGoodbye!!\n")
            break

        else:
            print("Oops!! Incorrect input.")

    except ValueError:
        print("\nOops!! Please enter a number from the Menu.\n")