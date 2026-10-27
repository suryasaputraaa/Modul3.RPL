import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menghubungkan tombol simpan dengan fungsi simpan_data
        self.view.btn_simpan.configure(command=self.simpan_data)

        # Memuat data anggota saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Menghapus seluruh data yang tampil di tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data anggota dari Model
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data anggota ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def simpan_data(self):
        # Mengambil data dari kolom input
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Memeriksa apakah form masih kosong
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat anggota harus diisi!"
            )
            return

        # Menyimpan data anggota ke database
        try:
            berhasil = self.model.create_anggota(nama, alamat)

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data anggota berhasil disimpan!"
                )

                # Mengosongkan form setelah data disimpan
                self.view.entry_nama.delete(0, "end")
                self.view.entry_alamat.delete(0, "end")

                # Memuat ulang tabel
                self.muat_data_tabel()

            else:
                messagebox.showerror(
                    "Error",
                    "Data anggota gagal disimpan!"
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan saat menyimpan data: {e}"
            )

    def run(self):
        # Menjalankan tampilan aplikasi
        self.view.mainloop()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()