import os
from cryptography.fernet import Fernet

# יצירת מפתח הצפנה ושמירתו לקובץ
key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# טעינת המפתח
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# יצירת אובייקט הצפנה
cipher = Fernet(key)

# הצפנת כל קבצי ה-.sql בתיקייה ובתתי-התיקיות
directory = "."  # התיקייה הנוכחית, ניתן לשנות את הנתיב לתיקייה אחרת

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".sql"):
            file_path = os.path.join(root, filename)

            # קריאת תוכן הקובץ להצפנה
            with open(file_path, "rb") as file:
                file_data = file.read()

            # הצפנת הנתונים
            encrypted_data = cipher.encrypt(file_data)

            # שמירת הקובץ המוצפן (משנים את הסיומת ל-.enc)
            encrypted_filename = f"{file_path}.enc"
            with open(encrypted_filename, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)

            # מחיקת הקובץ המקורי אם רוצים (לא חובה)
            os.remove(file_path)

print("All .sql files have been encrypted, including in subdirectories.")
