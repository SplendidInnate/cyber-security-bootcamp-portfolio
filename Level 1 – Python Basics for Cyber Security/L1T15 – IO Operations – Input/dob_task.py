with open("DOB.txt", "r+") as file:
    lines = file.readlines()

names = []
birthdates = []

for line in lines:
    parts = line.strip().split()
    
    name = parts[0] + " " + parts[1]
    birthdate = " ".join(parts[2:])
    
    names.append(name)
    birthdates.append(birthdate)

#Names
print("Name")
for name in names:
    print(name)

print(" ")

#Birthdates
print("Birthdate")
for date in birthdates:
    print(date)
