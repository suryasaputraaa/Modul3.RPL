import tkinter.messagebox as messagebox

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()

        # Menghubungkan tombol Masuk dengan fungsi login
        self.view.btn_login.configure(command=self.login)

        # Tekan Enter untuk melakukan login
        self.view.entry_password.bind(
            "<Return>",
            lambda event: self.login()
        )

    def login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi!",
                parent=self.view
            )
            return

        # Memeriksa username dan password melalui UserModel
        user = self.model.autentikasi(username, password)

        if user:
            role = user["role"]

            if role not in ("admin", "anggota"):
                messagebox.showerror(
                    "Akses Ditolak",
                    "Role pengguna tidak dikenali.",
                    parent=self.view
                )
                return

            messagebox.showinfo(
                "Login Berhasil",
                f"Selamat datang, {username}!",
                parent=self.view
            )

            # Tutup halaman login
            self.view.destroy()

            # Buka aplikasi perpustakaan sesuai role
            self.buku_controller = BukuController(user_role=role)
            self.buku_controller.run()

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau password salah!",
                parent=self.view
            )

    def run(self):
        self.view.mainloop()