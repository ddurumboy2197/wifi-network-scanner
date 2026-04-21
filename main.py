import hashlib
import getpass

def password_hashing():
    print("Password Hashing Tool")
    print("---------------------")

    password = getpass.getpass("Enter your password: ")
    password = password.encode('utf-8')

    hash_object = hashlib.sha256(password)
    hashed_password = hash_object.hexdigest()

    print("Hashed Password: ", hashed_password)

password_hashing()
