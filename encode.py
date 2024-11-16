import os
from cryptography.fernet import Fernet

# Generate an encryption key and save it to a file
key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
  key_file.write(key)

# Load the key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Create an encryption object
cipher = Fernet(key)

# Encrypt all .sql files in the directory and subdirectories
directory = "."  # Current directory; change the path if needed

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".sql"):
            file_path = os.path.join(root, filename)

            # Read the file content for encryption
            with open(file_path, "rb") as file:
                file_data = file.read()

            # Encrypt the data
            encrypted_data = cipher.encrypt(file_data)

            # Save the encrypted file (change extension to .enc)
            encrypted_filename = f"{file_path}.enc"
            with open(encrypted_filename, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)

            # Remove the original file if desired (optional)
            os.remove(file_path)

print("All .sql files have been encrypted, including in subdirectories.")
