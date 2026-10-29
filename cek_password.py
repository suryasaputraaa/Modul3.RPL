import hashlib
from models.user_model import UserModel

model = UserModel()

username = input("Masukkan username (petugas/mahasiswa): ")
password = input("Masukkan password yang biasa digunakan: ")

cursor = model.conn.cursor()
cursor.execute(
    "SELECT password FROM users WHERE username = %s",
    (username,)
)
hasil = cursor.fetchone()
cursor.close()

if hasil:
    password_input = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    if password_input == hasil[0]:
        print("Password cocok dengan database.")
    else:
        print("Password tidak cocok dengan database.")
else:
    print("Username tidak ditemukan.")