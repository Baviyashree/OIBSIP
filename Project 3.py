import string
import random

def generate_password(length, letters=True, numbers=True, symbols=True):
    characters = ""

    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Please choose at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    letters = input("Include letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, letters, numbers, symbols)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
