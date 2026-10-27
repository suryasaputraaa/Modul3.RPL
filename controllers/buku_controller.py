import tkinter.messagebox as messagebox
from models.buku_model import bukumodel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = bukumodel()
        self.view = BukuView()

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Memuat data buku saat aplikasi dibuka
        self.muat_data_tabel()

    def run(self):
        self.view.mainloop()
        
    def muat_data_tabel(self):
        # Mengosongkan tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data buku dari Model
        data_buku = self.model.get_all_buku()

        # Memasukkan data ke tabel
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
        # Mengambil data dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Memeriksa form kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Menyimpan data buku
        try:
            berhasil = self.model.create_buku(judul, penulis, tahun)

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil disimpan!"
                )
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Data buku gagal disimpan."
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan: {e}"
            )

    def perbarui_data(self):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku pada tabel terlebih dahulu!"
            )
            return

        # Mengambil data dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")
        id_buku = data[0]

        # Mengambil data dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Jika form masih kosong, isi form dengan data terpilih
        if not judul and not penulis and not tahun:
            self.view.entry_judul.insert(0, data[1])
            self.view.entry_penulis.insert(0, data[2])
            self.view.entry_tahun.insert(0, data[3])

            messagebox.showinfo(
                "Informasi",
                "Data buku terpilih sudah dimasukkan ke form. "
                "Ubah data yang diperlukan, lalu klik Perbarui Data lagi."
            )
            return

        # Memeriksa kelengkapan form
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi untuk memperbarui data!"
            )
            return

        # Memperbarui data melalui Model
        try:
            berhasil = self.model.update_buku(
                id_buku,
                judul,
                penulis,
                tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil diperbarui!"
                )
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Data buku gagal diperbarui."
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan: {e}"
            )

    def hapus_data(self):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku pada tabel yang ingin dihapus!"
            )
            return

        # Mengambil ID buku dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")
        id_buku = data[0]
        judul = data[1]

        # Meminta konfirmasi sebelum menghapus
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Apakah kamu yakin ingin menghapus buku '{judul}'?"
        )

        if not konfirmasi:
            return

        # Menghapus data melalui Model
        try:
            berhasil = self.model.delete_buku(id_buku)

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!"
                )
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Data buku gagal dihapus."
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan: {e}"
            )

    def bersihkan_form(self):
        # Mengosongkan seluruh kolom input
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")


if __name__ == "__main__":
    app = BukuController()
    app.view.mainloop()