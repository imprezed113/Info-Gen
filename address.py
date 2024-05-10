import string
import random


#Sets values for street name and number
streets = ["Main Street", "Oak Avenue", "Elm Road", "Cedar Lane", "Maple Drive"]
numbers = [str(random.randint(1, 1000)) for _ in range(5)]
zip = str(random.randint(10000,99999))
city = ["Tampa", "Ocala", "Miami", "Orlando", "Saint Petersburg"]


# Generate a random street address
random_street = random.choice(streets)
random_number = random.choice(numbers) 
random_zip = zip
city = random.choice(city)
state = "FL"
random_address = f"{random_number} {random_street} {city} {state} {zip}"

# Prints values
for _ in range (10):
    print(random_address)