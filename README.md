## What You Need to Know:

This folder contains two essential files:
1. **encryption_key.key** - the encryption key.
2. **clone and decode.bat** - this script will pull the latest queries from the Git repo, create a new virtual environment (venv) with all the necessary Python libraries, and decrypt the queries using the encryption key. After running this, you'll be set up and ready to work with the queries.

## How to Add and Upload New Queries

If you decide to add new queries and want to upload them to Git:
1. Put them inside the  **SQL Queries** folder in the appropriate place.
2. Simply double-click **encode and upload to git.bat**.
3. A window will open where you'll need to add a commit message for Git.
    a. press the "i" key on keyboard.  
    b. write your message.
    c. press the **esc** key, and then press **:** and then **wq** and then **enter**.

This script will automatically encrypt your new queries and upload them to the Git repository.

## After Finishing Work - Cleaning Up

When you're done, please remember to double-click **clean.bat**. This script will remove all queries from your folder to prevent any desynchronization after other users' updates.

## Summary

- **Import Queries**: Double-click on `clone and decode.bat`.
- **Upload Queries**: Double-click on `encode and upload to git.bat`, then add a commit message.
- **Clean Up**: Double-click on `clean.bat`.