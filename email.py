import string
import random

def generate_random_email():
# Generate a random username
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
# Generate a random domain
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + ".com"
# Combine the username and domain to create an email address
    email = username + "@" + domain
    return email

# Generate a list of 12,000 random email addresses
random_emails = [generate_random_email() for _ in range(12000)]

# Print or export the list as needed for your demonstration
for email in random_emails:
    print(email)