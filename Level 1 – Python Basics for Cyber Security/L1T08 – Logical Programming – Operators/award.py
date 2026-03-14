#Auto-Grade Task:

print("Please enter all the times in minutes taken to complete each competition")
swimming = int(input("Minutes taken in Swimming: "))
cycling = int(input("Minutes taken in Cycling: "))
running = int(input("Minutes taken in Running: "))
print(" ")
total_time = swimming+cycling+running
print(f"Total time taken for the triathlon: {total_time} minutes")

if total_time >=0 and total_time <= 100:
    print("Award Received: Provincial Colours")
elif total_time >= 101 and total_time <=105:
    print("Award Received: Provincial Half Colours")
elif total_time >= 106 and total_time <=110:
    print("Award Received: Provincial Scroll")
else:
    print("Award Received: No Award")