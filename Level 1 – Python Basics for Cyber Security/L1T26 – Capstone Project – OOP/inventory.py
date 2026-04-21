# Capstone Project L1T26:

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """ This constructor is for storing shoe details."""
        # Shoe attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """ This method is for returning the cost of the shoe."""
        
        return self.cost

    def get_quantity(self):
        """ This method is for returning the quantity of the shoes."""
        return self.quantity

    def __str__(self):
        """ This method is for returning the shoe details as a string."""
        return(
            f"Country: {self.country}, "
            f"Code: {self.code}, "
            f"Product: {self.product}, "
            f"Cost: {self.cost}, "
            f"Quantity: {self.quantity}"
              )

#=============Shoe list===========
'''The list is used to store a list of objects of shoes.'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    """ This function is for reading shoe data from inventory.txt."""
    try:
        with open("inventory.txt", "r") as file:
            next(file) # Skip the Heading line

            for line in file:
                data = line.strip().split(",")

                # Add valid rows
                if len(data) == 5: 
                    country, code, product, cost, quantity = data
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)

        print("\nShoe data loaded successfully.\n")

    except FileNotFoundError:
        print("\nError: inventory.txt file not found.\n")

    except Exception as error:
        print(f"\nAn error occured: {error}\n")

def capture_shoes():
    """ This function is for capturing a new shoe from user input."""
    
    try:
        country = input("Enter country: ").title()
        code = input("Enter code: ").upper()
        product = input("Enter product name: ").title()
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        new_shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(new_shoe)

        # Saving the new shoe into the txt file
        with open("inventory.txt", "a") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")
        print("\nNew shoe added successfully.\n")

    except ValueError:
        print("\nInvalid input. Cost must be a number and quantity must be a whole number.\n")

def view_all():
    """ This function is for showing all shoes in the shoe list."""

    if len(shoe_list) == 0:
        print("\nThere are no shoes to display.\n")
    else:
        print("\nAll Shoe Details: ")
        for shoe in shoe_list:
            print(shoe)
        print()

def update_file():
    """This function is for rewriting the inventory.txt file with updated data."""

    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")

        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{int(shoe.cost)},{shoe.quantity}\n"
            )

def re_stock():
    """ 
    This function is for finding a shoe,
    with the lowest quality and updating it.
    """
    if len(shoe_list) == 0:
        print("\nNo shoe data available.\n")
        return
    
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)

    print("\nShoe that needs restocking: ")
    print(lowest_shoe)

    choice = input("Do you want to add stock for this shoe? (Yes/No): ").lower()

    if choice == "yes":
        try:
            added_qty = int(input("How many shoes would ypu like to add? "))
            lowest_shoe.quantity += added_qty

            update_file()

            print("\nStock updated successfully.\n")
            print(lowest_shoe)

        except ValueError:
            print("\nInvalid quantity entered.\n")
    else:
        print("\nNo stock was added.\n")

def search_shoe():
    """ This function is for searching for a shoe by code."""

    if len(shoe_list) == 0:
        print("\nNo shoe data available.\n")
        return
    
    search_code = input("Enter the shoe code to search: ").upper()

    for shoe in shoe_list:
        if shoe.code == search_code:
            print("\nShoe found: ")
            print(shoe)
            return shoe
        
    print("\nShoe not found.\n")

def value_per_item():
    """This function is for calculating the total value for each shoe item."""

    if len(shoe_list) == 0:
        print("\nNo shoe data available.\n")
    else:
        print("\nValue per item:")
        for shoe in shoe_list:
            value = shoe.get_cost() * shoe.get_quantity()
            print(f"{shoe.product} ({shoe.code}) = {value}")
        print()

def highest_qty():
    """This function is for finding the shoe with the highest quantity."""

    if len(shoe_list) == 0:
        print("\nNo shoe data available.\n")
        return

    # Finds the shoe with the highest quantity
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

    print("\nThis shoe is for sale:")
    print(highest_shoe)

#==========Main Menu=============

read_shoes_data()

while True:
    print("========== Shoe Inventory Menu ==========")
    print("1. View all shoes")
    print("2. Capture a new shoe")
    print("3. Re-stock shoe")
    print("4. Search for a shoe")
    print("5. Show value per item")
    print("6. Show shoe with highest quantity")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("\nGoodbye!!\n")
        break

    else:
        print("\nInvalid choice. Please try again.\n")
