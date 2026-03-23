#Auto-Grade Task 2:

menu = ["Beef Burger", "Dagwood Sandwich", "Pizza", "Pie"]

stock = {"Beef Burger" : 80,
         "Dagwood Sandwich" : 95,
         "Pizza" : 100,
         "Pie" : 100
        }

price = {"Beef Burger" : 110,
         "Dagwood Sandwich" : 85,
         "Pizza" : 180,
         "Pie" : 55
        }

total_stock = 0

for item in menu:
    item_value = (stock[item] * price[item])

    total_stock += item_value

print(f"The Total Worth of the Stock is: R{total_stock}")