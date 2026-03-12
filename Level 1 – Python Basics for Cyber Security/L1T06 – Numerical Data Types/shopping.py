#Practical Task 2:

print("Enter the names of your three products")

product_1 = input("Product 1: ")
product_2 = input("Product 2: ")
product_3 = input("Product 3: ")
print(" ")

print("Please Enter the Price of each Product")
price_1 = float(input(f"Enter Price for {product_1}: R"))
price_2 = float(input(f"Enter Price for {product_2}: R"))
price_3 = float(input(f"Enter Price for {product_3}: R"))

sum = price_1+ price_2+price_3
average = round(sum/3)
print(" ")
print(f"The total of {product_1}, {product_2}, {product_3} is R{sum:.2f} and the average price of the items is {average:.2f}")