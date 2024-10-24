from cryptography.fernet import Fernet
import os

# טעינת מפתח ההצפנה
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# יצירת אובייקט לפענוח
cipher = Fernet(key)

# פענוח כל קבצי ה-.sql.enc בתיקייה ובתתי-התיקיות
directory = "."  # התיקייה הנוכחית, ניתן לשנות לתיקייה אחרת אם יש צורך

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".sql.enc"):
            file_path = os.path.join(root, filename)

            # קריאת תוכן הקובץ המוצפן
            with open(file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()

            # פענוח הנתונים
            try:
                decrypted_data = cipher.decrypt(encrypted_data)

                # שחזור שם הקובץ המקורי (הסרת הסיומת .enc)
                decrypted_filename = file_path.replace(".enc", "")
                with open(decrypted_filename, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_data)

                # מחיקת הקובץ המוצפן לאחר פענוח מוצלח
                os.remove(file_path)

                print(f"File decrypted and encrypted file deleted: {decrypted_filename}")

            except Exception as e:
                print(f"Decryption failed for {file_path}: {e}")  # הדפסה של פרטי השגיאה

print("All .sql.enc files have been decrypted, including in subdirectories.")
