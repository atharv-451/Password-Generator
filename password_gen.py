import random
import string

def generate_password(length=10):
    # Define characters for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the characters in the password
    random.shuffle(password)

    # Convert the list to a string
    password_str = ''.join(password)

    return password_str

if __name__ == "__main__":
    # You can specify the desired length of the password (default is 12)
    password_length = 16
    generated_password = generate_password(password_length)

    print(f"Generated Password: {generated_password}")
