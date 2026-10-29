import tkinter.messagebox as messagebox

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()

        # Menghubungkan tombol login
        self.view.btn_login.configure(command=self.proses_login)

        # Login menggunakan tombol Enter
        self.view.entry_password.bind(
            "<Return>",
            lambda event: self.proses_login()
        )

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan Password wajib diisi!",
                parent=self.view
            )
            return

        # Memeriksa kredensial melalui UserModel
        user = self.model.autentikasi(username, password)

        if not user:
            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah!",
                parent=self.view
            )
            return

        role = user["role"]

        if role not in ("admin", "anggota"):
            messagebox.showerror(
                "Login Gagal",
                "Role pengguna tidak dikenali.",
                parent=self.view
            )
            return

        messagebox.showinfo(
            "Login Berhasil",
            f"Selamat datang, {user['username']} ({role})!",
            parent=self.view
        )

        # Tutup halaman login
        self.view.destroy()

        # Buka aplikasi perpustakaan sesuai role
        self.app_utama = BukuController(user_role=role)
        self.app_utama.run()

    def run(self):
        self.view.mainloop()