import bcrypt

def hash_password(password):
    encoded_password = password.encode("utf-8")

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded_password, salt)

    return hashed

user_password = input("Please Enter a Password to Hash: ")

hashed_password = hash_password(user_password)

print(f"Your Hashed Password is: {hashed_password}")
