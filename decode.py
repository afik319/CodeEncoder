from cryptography.fernet import Fernet
import os

# Load the encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Create a decryption object
cipher = Fernet(key)

# Decrypt all .sql.enc files in the directory and subdirectories
directory = "."  # Current directory

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".sql.enc"):
            file_path = os.path.join(root, filename)

            # Read the encrypted file content
            with open(file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()

            # Decrypt the data
            try:
                decrypted_data = cipher.decrypt(encrypted_data)

                # Restore the original filename (remove .enc extension)
                decrypted_filename = file_path.replace(".enc", "")
                with open(decrypted_filename, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_data)

                # Delete the encrypted file after successful decryption
                os.remove(file_path)

                print(f"File decrypted and encrypted file deleted: {decrypted_filename}")

            except Exception as e:
                print(f"Decryption failed for {file_path}: {e}")  # Print the error details

print("All .sql.enc files have been decrypted, including in subdirectories.")
