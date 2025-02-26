import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
