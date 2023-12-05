#STRONG PASSWORD GENERATOR
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        desired_length = int(input("Enter the desired length for the password: "))
        if desired_length <= 0:
            print("Please enter a length greater than 0.")
        else:
            password = generate_password(desired_length)
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid length (a positive integer).")

if __name__ == "__main__":
    main()