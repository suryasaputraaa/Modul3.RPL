from models.user_model import UserModel

model = UserModel()

username = "admin_baru"
password = input("Masukkan password untuk akun admin baru: ")

berhasil = model.register_user(username, password, "admin")

if berhasil:
    print("Akun admin berhasil dibuat!")
    print("Username: admin_baru")
    print("Gunakan password yang baru saja kamu masukkan untuk login.")
else:
    print("Akun gagal dibuat. Periksa pesan error di terminal.")