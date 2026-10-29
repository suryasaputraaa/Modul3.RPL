import tkinter.messagebox as messagebox

from models.buku_model import bukumodel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role.lower()
        self.model = bukumodel()
        self.view = BukuView()

        # Menampilkan role pada judul jendela
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode {self.user_role.upper()}"
        )

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)

        # Hak akses: hanya admin yang boleh mengelola data buku
        if self.user_role != "admin":
            self.view.btn_simpan.configure(
                state="disabled",
                text="Khusus Admin"
            )
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data buku
        self.muat_data_tabel()

    def muat_data_tabel(self):
        """Menampilkan seluruh data buku pada tabel."""
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        """Menyimpan data buku baru."""
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya admin yang boleh menambah data buku!",
                parent=self.view
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!",
                parent=self.view
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!",
                parent=self.view
            )
            return

        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!",
                parent=self.view
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal disimpan.",
                parent=self.view
            )

    def perbarui_data(self):
        """Memperbarui data buku yang dipilih."""
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya admin yang boleh memperbarui data buku!",
                parent=self.view
            )
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku pada tabel terlebih dahulu!",
                parent=self.view
            )
            return

        nilai = self.view.tabel.item(pilihan[0], "values")
        id_buku = nilai[0]

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Isi semua kolom dengan data terbaru!",
                parent=self.view
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!",
                parent=self.view
            )
            return

        berhasil = self.model.update_buku(
            id_buku,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!",
                parent=self.view
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal diperbarui.",
                parent=self.view
            )

    def hapus_data(self):
        """Menghapus data buku yang dipilih."""
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Hanya admin yang boleh menghapus data buku!",
                parent=self.view
            )
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku pada tabel terlebih dahulu!",
                parent=self.view
            )
            return

        nilai = self.view.tabel.item(pilihan[0], "values")
        id_buku = nilai[0]
        judul = nilai[1]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus buku '{judul}'?",
            parent=self.view
        )

        if not konfirmasi:
            return

        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!",
                parent=self.view
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal dihapus.",
                parent=self.view
            )

    def bersihkan_form(self):
        """Mengosongkan seluruh kolom input."""
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    def logout(self):
        """Keluar dari aplikasi dan kembali ke halaman login."""
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Logout",
            "Apakah kamu yakin ingin logout?",
            parent=self.view
        )

        if not konfirmasi:
            return

        # Tutup jendela perpustakaan
        self.view.destroy()

        # Kembali ke controller login utama
        from controllers.auth_controller import AuthController

        self.login_controller = AuthController()
        self.login_controller.run()

    def run(self):
        """Menjalankan jendela perpustakaan."""
        self.view.mainloop()