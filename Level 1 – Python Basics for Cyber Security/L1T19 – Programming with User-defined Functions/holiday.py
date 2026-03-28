# Auto-Grade Task:

# Variables & User inputs details
city_flight = input("Hello, Where are you flying to: \nCape Town: R1 500\nDurban: R1 350\nPretoria: R900\nJohannesburg: R940\nCity: ")
destination = city_flight
num_nights = int(input("Number of nights you will be staying: "))
rental_days = int(input("Number of days for which you will be renting the car: "))

# Hotel Cost Function
def hotel_cost(num_nights): 
    accomodation = 900 * num_nights # Hotel Price Total logic calculation
    return accomodation

# Plane Cost Function
def plane_cost(city_flight):
    city = city_flight.lower()

    if city_flight == "cape town":
        return 1500

    elif city_flight == "durban":
        return 1350
        
    elif city_flight == "pretoria":
        return 900
    
    elif city_flight == "johannesburg":
        return 940

    else:
        return 1750

# Car rental cost function 
def car_rental(rental_days):
    rental_cost = 400 * rental_days
    return rental_cost

# Holiday cost function
def holiday_cost(num_nights, city_flight, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total

# Calculation Variables
hotel = hotel_cost(num_nights)
flight = plane_cost(city_flight)
car = car_rental(rental_days)
total_cost = holiday_cost(num_nights, city_flight, rental_days)

print(" ") # One line space for a neat display
print("-" * 30 + " " + "Holiday Cost Details" + " " + "-" * 30) # Heading for Cost details
print(" ")

# Detailed print out
print(f"Your Holiday City is: {city_flight.upper()} & Flight Cost is: R{flight:.2f}")
print(f"Your Hotel Cost is: R{hotel:.2f}")
print(f"Your Car Rental Cost is: R{car:.2f}")
print(" ")
print(f"Total Holiday Cost: R{total_cost:.2f}")

