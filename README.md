# SQL Encryption & Decryption Utility

## Overview
This project provides a simple tool for encrypting and decrypting `.sql` files. The tool can traverse through the specified directory and all its subdirectories, encrypting or decrypting `.sql` files.

The tool consists of two Python scripts:
1. `encode.py`: Encrypts all `.sql` files in the directory and its subdirectories.
2. `decode.py`: Decrypts all `.sql.enc` files in the directory and its subdirectories.

### Encryption Key
The encryption key is generated the first time the encryption script runs and is stored in a file named `encryption_key.key`. This key is used for both encrypting and decrypting the files. **Make sure to keep this key safe** – if it is lost, you will not be able to decrypt the files.

## Files

### 1. `encode.py`
This script:
- Generates a new encryption key (`encryption_key.key`) if one does not exist.
- Encrypts all `.sql` files in the current directory and its subdirectories.
- Saves the encrypted files with a `.enc` extension (e.g., `file.sql` becomes `file.sql.enc`).
- Optionally deletes the original `.sql` files after encryption.

### 2. `decode.py`
This script:
- Loads the previously generated encryption key from the `encryption_key.key` file.
- Decrypts all `.sql.enc` files in the current directory and its subdirectories.
- Restores the original `.sql` files by removing the `.enc` extension.
- Deletes the encrypted files (`.enc`) after successful decryption.

## How to Use
1. **Encrypt Files**: Double click `encode.bat` to encrypt all `.sql` files.
2. **Decrypt Files**: Double click `decode.bat` to decrypt all `.sql.enc` files.
