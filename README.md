# SQL Queries Encryption and Decryption Project

## Overview
This project enables secure storage and management of SQL queries using encryption and decryption. It is designed for collaborative work, ensuring synchronization between multiple users working on the same repository.

---

## Setup and First-Time Use
1. **Clone the Repository**:
   - Run `clone and decode.bat` to clone this repository into a the current local folder.

2. **Update Repository Address**:
   - Open `encode and upload to git.bat`.
   - Replace the repository URL with the address of the repository you want to use.

3. **Keep These Essential Files in the Folder**:
   - `encryption_key.key` (very important – losing this key means losing access to your encrypted files).
   - `venv.bat` (saves time during subsequent clones by reusing the environment initialized during the first setup).
   - `clone and decode.bat` (to update and decrypt queries).

---

## Workflow

### 1. Pull and Decrypt Queries
- Double-click **`clone and decode.bat`**.
  - This will pull the latest queries from the repository, set up the environment (if needed), and decrypt `.sql.enc` files into `.sql` files.

### 2. Add or Update Queries
- Place your `.sql` files in the **current folder** or any **subfolder**.
- Make sure all files you want to encrypt are in the folder.

### 3. Encrypt and Upload
- Double-click **`encode and upload to git.bat`**.
  - This will:
    1. Encrypt all `.sql` files in the folder.
    2. Upload the encrypted files to your repository.
    3. Automatically delete the decrypted `.sql` files to prevent desynchronization.

---

## Important Notes
1. **Keep Essential Files**:
   - Ensure the following files remain in the folder:
     - `encryption_key.key`
     - `venv.bat`
     - `clone and decode.bat`
   - Do not delete these files, as they are necessary for the workflow.

2. **Backup Your Encryption Key**:
   - Losing `encryption_key.key` means losing access to your encrypted queries permanently.

3. **Synchronization**:
   - The workflow ensures no conflicts occur when multiple users work on the same repository by clearing the folder after encryption and upload.

---

## Summary of Commands

- **Pull and Decrypt**: Double-click `clone and decode.bat`.
- **Add and Encrypt Queries**: Place `.sql` files in the folder and double-click `encode and upload to git.bat`.
- **Keep Essential Files**: Ensure `encryption_key.key`, `venv.bat`, and `clone and decode.bat` remain in the folder.
