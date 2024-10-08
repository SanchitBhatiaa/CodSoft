import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password has at least one character from each category
    if length < 4:
        print("Password length should be at least 4 for complexity.")
        return None

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the result to ensure randomness
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Input: password length
    length = int(input("Enter the desired length of the password (minimum 4): "))

    # Generate and display the password
    password = generate_password(length)
    
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
