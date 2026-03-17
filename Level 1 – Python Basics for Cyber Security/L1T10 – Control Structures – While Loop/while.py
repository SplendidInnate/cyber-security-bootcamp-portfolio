#L1T10 Auto-Grade Task:

#Declarations for storing variables
total = 0
count = 0

#while loop
while True:
    number = int(input("Enter a number OR (-1 to Stop): ")) #user input
    if number == -1: #-1 to break the loop
        break

    total += number #adding number to the total
    count += 1 #increase the count of numbers entered

    if count > 0:
        average = total/count #average calculation

        print(f"The Average is: {average:.0f}")

    else: 
        print("Invalid or No Numbers Entered.") 