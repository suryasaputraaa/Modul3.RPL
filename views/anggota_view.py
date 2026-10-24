import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("800x450")

        # ==========================================
        # KONFIGURASI GRID UTAMA
        # ==========================================

        # 1 baris dan 2 kolom
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI: FORM DATA ANGGOTA
        # ==========================================

        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # ==========================================
        # INPUT NAMA ANGGOTA
        # ==========================================

        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota"
        )
        self.entry_nama.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==========================================
        # INPUT ALAMAT
        # ==========================================

        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat"
        )
        self.entry_alamat.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        # ==========================================
        # TOMBOL SIMPAN
        # ==========================================

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green"
        )
        self.btn_simpan.pack(
            pady=20,
            padx=15,
            fill="x"
        )

        # ==========================================
        # FRAME KANAN: TABEL DATA ANGGOTA
        # ==========================================

        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # ==========================================
        # KOMPONEN TABEL
        # ==========================================

        kolom = (
            "id",
            "nama",
            "alamat"
        )

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        # ==========================================
        # HEADER TABEL
        # ==========================================

        self.tabel.heading(
            "id",
            text="ID"
        )

        self.tabel.heading(
            "nama",
            text="Nama"
        )

        self.tabel.heading(
            "alamat",
            text="Alamat"
        )

        # ==========================================
        # LEBAR KOLOM TABEL
        # ==========================================

        self.tabel.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabel.column(
            "nama",
            width=180
        )

        self.tabel.column(
            "alamat",
            width=250
        )

        # Menampilkan tabel
        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


# ==========================================
# BLOK EKSEKUSI
# ==========================================

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()