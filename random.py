import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("How many passwords would you like to generate?")
    num_passwords = int(input("Enter number of passwords: "))
    length = int(input("Enter password length: "))

    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i+1}: {password}")

if _name_ == "_main_":
    main()