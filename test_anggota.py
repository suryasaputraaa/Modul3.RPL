from models.anggota_model import AnggotaModel

model_anggota = AnggotaModel()

# 1. Menguji fungsi Create (Menambah anggota baru)
print("Menambahkan data anggota baru...")
model_anggota.create_anggota("shadiq", "kabonena")
print("Data anggota berhasil disimpan ke MySQL Laragon!")

# 2. Menguji fungsi Read (Menampilkan data anggota)
print("\n=== DAFTAR ANGGOTA PERPUSTAKAAN ===")
daftar_anggota = model_anggota.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - Alamat: {anggota['alamat']}")