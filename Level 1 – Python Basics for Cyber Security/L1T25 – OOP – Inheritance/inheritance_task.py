# Practical Task L1T25 (Task 1):

class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting:", self.contact_website)

    def HeadOffice_location(self):
        "This method displays/prints the head office location."
        print("Head Office Location: Cape Town")
    
class OOPCourse(Course):
    def __init__(self):
        """ This constructor is for setting default values."""
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse" 
            
    def trainer_details(self):
        """ This method is for showing course description and trainer."""
        print("Course description:", self.description)
        print("Trainer:", self.trainer)

    def show_course_id(self):
        """ This method is for showing Course iD."""
        print("Course iD: #12345")

# Object
course_1 = OOPCourse()

# Calling Methods
course_1.contact_details()
course_1.HeadOffice_location()
course_1.trainer_details()
course_1.show_course_id()
