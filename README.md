# SQL Queries Encryption and Decryption Project

## Overview
This project provides a simple way to securely store and share SQL query files. It includes encryption and decryption scripts wrapped in easy-to-use `.bat` files for convenience.

---

## Files in the Project

- **`encode.py`**: Encrypts `.sql` files in the current directory and its subdirectories (triggered by `encode.bat`).
- **`decode.py`**: Decrypts `.sql.enc` files in the current directory and its subdirectories (triggered by `clone and decode.bat`).
- **`encryption_key.key`**: The encryption key used for both encryption and decryption. Automatically generated if missing.

---

## How to Use

### 1. Import and Decrypt Queries
To pull the latest queries from the Git repository, set up the environment, and decrypt them:
1. Double-click **`clone and decode.bat`**.
2. This script will:
   - Pull the latest updates from the Git repository.
   - Create a virtual environment (`venv`) and install required libraries.
   - Decrypt the queries using `decode.py`.

Once the script finishes, you will have the decrypted `.sql` files ready for use.

### 2. Add and Encrypt New Queries
To add new queries and upload them securely:
1. Place the new `.sql` files in the appropriate directory.
2. Double-click **`encode and upload to git.bat`**.
3. A terminal window will open where you can add a commit message for Git:
   - Press the `i` key to enter "insert mode."
   - Write your commit message.
   - Press `Esc`, then type `:wq` and press Enter to save and exit.
4. The script will:
   - Encrypt the new `.sql` files using `encode.py`.
   - Commit and push the changes to the Git repository.

### 3. Clean Up After Work
To prevent synchronization issues after updates by other users:
1. Double-click **`clean.bat`**.
2. This script will remove all decrypted queries from your directory, leaving only encrypted files and necessary scripts.

---

## Important Notes
- **Do not delete the `encryption_key.key` file**, as it is required for both encryption and decryption.
- Ensure the `encryption_key.key` file is stored securely to prevent unauthorized access.
- Backup your key file to avoid losing access to encrypted files.

---

## Summary
- **Import and Decrypt Queries**: Double-click `clone and decode.bat`.
- **Add and Encrypt Queries**: Double-click `encode and upload to git.bat`, then add a commit message.
- **Clean Up**: Double-click `clean.bat`.
