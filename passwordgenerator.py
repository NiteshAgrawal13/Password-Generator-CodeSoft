import random
import string

def generate_password(length):
    char_words= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char_words) for _ in range(length))
    return password

def main():
    try:
        desired_length = int(input("Please enter the length of password\n"))
        if desired_length <= 0:
            print("please enter length greater tha 0")
        else:
            password=generate_password(desired_length)
            print("Generated Password is:\n",password)
    except ValueError:
        print("Enter valid length")
if __name__ == "__main__":
    main()