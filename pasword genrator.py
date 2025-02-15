import random
import string

def generate_password(length=12):
    """
    Generates a secure, random password.
    :param length: Length of the password (default is 12 characters)
    :return: A randomly generated password
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Character pools
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    # Ensure the password has at least one character from each pool
    mandatory = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random choices from all pools
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    remaining_length = length - len(mandatory)
    random_characters = random.choices(all_characters, k=remaining_length)
    
    # Combine and shuffle the characters
    password_list = mandatory + random_characters
    random.shuffle(password_list)
    
    # Convert list to string and return
    return ''.join(password_list)

# User input for password length
try:
    user_length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(user_length)
    print(f"Your secure password is: {password}")
except ValueError as e:
    print(f"Error: {e}")
