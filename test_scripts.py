import unittest
import os
from cryptography.fernet import Fernet
from main import (  
    write_to_file, read_from_file, 
    generate_and_save_key, load_key, 
    encrypt_file, decrypt_file
)

class TestFileEncryption(unittest.TestCase):
    def setUp(self):
        """Set up test files and key for testing."""
        self.key_file = 'test_key.key'
        self.original_file = 'test_patient.jpg'
        self.encrypted_file = 'test_encrypted_patient.jpg'
        self.decrypted_file = 'test_decrypted_patient.jpg'
        self.test_data = b"This is a test file content."

        write_to_file(self.original_file, self.test_data)

    def tearDown(self):
        """Clean up test files."""
        for file in [self.key_file, self.original_file, self.encrypted_file, self.decrypted_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_key_generation_and_loading(self):
        """Test key generation and loading."""
        key = generate_and_save_key(self.key_file)
        self.assertTrue(os.path.exists(self.key_file), "Key file was not created.")
        loaded_key = load_key(self.key_file)
        self.assertEqual(key, loaded_key, "Loaded key does not match the generated key.")

    def test_encryption_and_decryption(self):
        """Test encryption and decryption of files."""
        # Generate a key
        key = generate_and_save_key(self.key_file)

        # Encrypt the file
        encrypt_file(self.original_file, self.encrypted_file, key)
        self.assertTrue(os.path.exists(self.encrypted_file), "Encrypted file was not created.")

        # Decrypt the file
        decrypt_file(self.encrypted_file, self.decrypted_file, key)
        self.assertTrue(os.path.exists(self.decrypted_file), "Decrypted file was not created.")

        # Verify content matches original
        decrypted_data = read_from_file(self.decrypted_file)
        self.assertEqual(self.test_data, decrypted_data, "Decrypted content does not match original.")

    def test_invalid_key_decryption(self):
        """Test decryption with an invalid key."""
        # Generate two separate keys
        key1 = generate_and_save_key(self.key_file)
        key2 = Fernet.generate_key()  # A different key

        # Encrypt with one key
        encrypt_file(self.original_file, self.encrypted_file, key1)

        # Attempt decryption with a different key
        with self.assertRaises(Exception):
            decrypt_file(self.encrypted_file, self.decrypted_file, key2)

if __name__ == "__main__":
    unittest.main()
