# Practical Task L1T25 (Task 2):

# User Input
name = input("Please enter Name: ").title()
age = int(input("Please enter Age: "))
hair_color = input("Please enter Hair Color: ").capitalize()
eye_color = input("Please enter Eye Color: ").capitalize()

# Parent Class
class Adult: 
    def __init__(self, name, age, eye_color, hair_color):
        """ This constructor is for storing person details."""
        # Class attributes
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        """This method is for showing the person can drive."""
        print(f"\n{self.name} is old enough to drive.")

# Subclass of the Adult class: Child Class
class Child(Adult):
    def can_drive(self): # Override the can_drive() method.
        """This method overrides the parent method."""
        print(self.name, "is too young to drive.")

# Logic to create correct object
if age >= 18:
    person = Adult(name, age, eye_color, hair_color)
else:
    person = Child(name, age, eye_color, hair_color)

# Call method
person.can_drive()
