import random
import string

def generate_password(length=12):
    a= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(a) for _ in range(length))
    return password

if __name__ == "__main__":
    passlen = int(input("Enter the desired password length: "))
    generatedpassword = generate_password(passlen)
    print("Generated Password:", generatedpassword)