# pip install cryptography

# secret key generation
from cryptography.fernet import Fernet

key = Fernet.generate_key()
# print(key)

# Encryption
fernet = Fernet(key)

# wrting key
with open('key.key', 'wb') as filekey:
    filekey.write(key)

# reading key
with open('key.key', 'rb') as filekey:
    key=filekey.read()

with open('patient.jpg', 'rb') as file:
    original_file = file.read()

encrypted = fernet.encrypt(original_file)

with open('encrypted patient.jpg', 'wb') as file:
    file.write(encrypted)


# DECRYPTION

fernet = Fernet(key)

with open('encrypted patient.jpg', 'rb') as file:
    encrypted_file = file.read()
    
decrypted = fernet.decrypt(encrypted_file)

with open('decrypted patient.jpg', 'wb') as file:
    file.write(decrypted)