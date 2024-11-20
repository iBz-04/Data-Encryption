from cryptography.fernet import Fernet

# Helper Functions
def write_to_file(filename, data, mode='wb'):
    """Writes data to a file."""
    with open(filename, mode) as file:
        file.write(data)

def read_from_file(filename, mode='rb'):
    """Reads data from a file."""
    with open(filename, mode) as file:
        return file.read()

# Key Management
def generate_and_save_key(key_filename):
    """Generates a key and saves it to a file."""
    key = Fernet.generate_key()
    write_to_file(key_filename, key)
    return key

def load_key(key_filename):
    """Loads a key from a file."""
    return read_from_file(key_filename)

# Encryption and Decryption
def encrypt_file(input_filename, output_filename, key):
    """Encrypts a file and saves the encrypted version."""
    fernet = Fernet(key)
    original_data = read_from_file(input_filename)
    encrypted_data = fernet.encrypt(original_data)
    write_to_file(output_filename, encrypted_data)

def decrypt_file(input_filename, output_filename, key):
    """Decrypts a file and saves the decrypted version."""
    fernet = Fernet(key)
    encrypted_data = read_from_file(input_filename)
    decrypted_data = fernet.decrypt(encrypted_data)
    write_to_file(output_filename, decrypted_data)

# Main Execution
if __name__ == "__main__":
    key_file = 'key.key'
    original_file = 'patient.jpg'
    encrypted_file = 'encrypted_patient.jpg'
    decrypted_file = 'decrypted_patient.jpg'

    # Generate or load key
    try:
        key = load_key(key_file)
    except FileNotFoundError:
        key = generate_and_save_key(key_file)

    # Encrypt and decrypt
    encrypt_file(original_file, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)
