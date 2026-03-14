#Challange:

string_fav = input("Please Enter Your Favourite Restaurant: ")
int_fav = int(input("PLease Enter Your Favourite Number: "))
print(" ")
print(string_fav)
print(int_fav)

print(int(string_fav))
"""
This will cause an error because the favourite restaurant is text which is a string variable data type, 
Python cannot convert normal words like "KFC" or "McDonalds" into an integer.
Integers can only be created from numeric values such as 1 to 10, or as long as it is a number/integer.
"""