import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation for strong passwords
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Step 1: User input
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Length must be a positive number!")
    else:
        # Step 2: Generate password
        new_password = generate_password(length)

        # Step 3: Display password
        print("Generated Password:", new_password)
except ValueError:
    print("Please enter a valid number!")
