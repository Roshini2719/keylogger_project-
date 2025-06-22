 #config.py
from cryptography.fernet import Fernet

# Generate and store a key only once
key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)
