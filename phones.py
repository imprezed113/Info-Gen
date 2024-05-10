import random
import string


def generate_random_phone_number():
    # Generate random area code (3 digits)
    area_code = str(random.randint(100, 999))
    
    # Generate random exchange code (3 digits)
    exchange_code = str(random.randint(100, 999))
    
    # Generate random line number (4 digits)
    line_number = str(random.randint(1000, 9999))
    
    # Format the phone number as (XXX) XXX-XXXX
    formatted_number = f"({area_code}) {exchange_code}-{line_number}"
    
    return formatted_number

# Generate and print a random phone number
random_phone_number = [generate_random_phone_number () for _ in range(12000)]
print(random_phone_number)