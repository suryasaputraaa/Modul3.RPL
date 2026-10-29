# Sistem Perpustakaan

Aplikasi desktop manajemen perpustakaan berbasis Python dengan arsitektur
**MVC (Model-View-Controller)**. Aplikasi ini digunakan petugas perpustakaan
untuk login dan mengelola data buku. Antarmuka dibangun dengan
**CustomTkinter**, data disimpan di **MySQL**, dan kualitas kode dijaga
melalui **CI/CD dengan GitHub Actions**.

## Struktur Direktori

```
Aplikasi ini menerapkan arsitektur MVC (Model-View-Controller):

Modul3.RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml      # Konfigurasi CI (flake8 + pytest)
├── config/
│   └── database.py              # Konfigurasi & koneksi ke MySQL
├── models/                      # MODEL: logika data & akses database
│   ├── anggota_model.py         # Data anggota perpustakaan
│   ├── buku_model.py            # Data buku
│   └── user_model.py            # Data pengguna & autentikasi
├── views/                       # VIEW: tampilan antarmuka (CustomTkinter)
│   ├── anggota_view.py          # Halaman anggota
│   ├── buku_view.py             # Halaman buku
│   └── login_view.py            # Halaman login
├── controllers/                 # CONTROLLER: penghubung model dan view
│   ├── anggota_controller.py    # Logika pengelolaan anggota
│   ├── auth_controller.py       # Logika autentikasi
│   ├── buku_controller.py       # Logika pengelolaan buku
│   └── login_controller.py      # Logika proses login
├── tests/                       # Unit test (pytest)
│   ├── test_auth.py             # Test hashing & autentikasi
│   └── test_buku.py             # Test pengambilan data buku
├── buat_akun.py                 # Skrip pembuatan akun pengguna
├── cek_password.py              # Skrip pengecekan password
├── test_anggota.py              # Skrip uji coba fitur anggota
├── test_model.py                # Skrip uji coba model
├── main.py                      # Titik masuk aplikasi
├── requirements.txt             # Daftar dependensi
├── .gitignore
└── README.md
```

## Panduan Instalasi & Konfigurasi Database MySQL

### 1. Prasyarat
- Python 3.11 atau lebih baru
- Git
- Laragon (untuk MySQL)

### 2. Clone repositori
```
git clone https://github.com/suryasaputraaa/Modul3.RPL.git
cd Modul3.RPL
```

### 3. Buat dan aktifkan virtual environment
```
python -m venv env
./env/Scripts/activate
```

### 4. Instal dependensi
```
pip install -r requirements.txt
```

### 5. Siapkan database MySQL
1. Buka **Laragon**, klik **Start All** hingga MySQL menyala.
2. Buka **HeidiSQL** (klik kanan Laragon > MySQL > HeidiSQL).
3. Buat database baru bernama `db_perpustakaan`:
   ```sql
   CREATE DATABASE db_perpustakaan;
   ```
4. Buat tabel yang dibutuhkan aplikasi (data pengguna dan data buku) atau
   impor berkas `.sql` yang tersedia.

### 6. Sesuaikan konfigurasi koneksi
Buka berkas koneksi database di folder `config/` dan pastikan nilainya
sesuai dengan MySQL di Laragon:

```python
self.host = "localhost"
self.db_name = "db_perpustakaan"
self.username = "root"
self.password = ""
```

## Cara Menjalankan Aplikasi

**Dari kode sumber:**
```
python main.py
```

**Dari berkas .exe:**
Unduh `AplikasiPerpustakaan.exe` dari halaman
[Releases](https://github.com/suryasaputraaa/Modul3.RPL/releases),
pastikan MySQL di Laragon sudah menyala, lalu klik dua kali berkas tersebut.

**Menjalankan unit test:**
```
pytest -v
```

**Membuat ulang berkas .exe:**
```
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```
Hasilnya ada di folder `dist/`.

## CI/CD

Setiap `push` atau `pull request` ke branch `main` akan menjalankan
pipeline GitHub Actions secara otomatis:
1. Checkout kode
2. Menyiapkan Python 3.11
3. Instal dependensi
4. Pengecekan kualitas kode dengan **flake8**
5. Unit testing dengan **pytest**