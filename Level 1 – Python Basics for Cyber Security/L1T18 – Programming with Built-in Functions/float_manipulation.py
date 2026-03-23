#Auto-Grade Task 1 (L1T18):

import statistics

floats = []

for i in range(10):
    user_input = float(input(f"Enter 10 floats/numbers (decimal/whole numbers) {i+1}: "))
    floats.append(user_input)

print(" ")
print(f"Sum of Numbers = {sum(floats)}")
print(f"Maximum of Numbers = {max(floats)}")
print(f"Minimum of Numbers = {min(floats)}")
print(f"Average/Mean of Numbers = {round(statistics.mean(floats),2)}")
print(f"Median of Numbers = {statistics.median(floats)}")