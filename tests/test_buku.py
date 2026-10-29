from unittest.mock import MagicMock
from models.buku_model import bukumodel


def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = bukumodel()

    # Membuat Mock untuk koneksi database
    model.conn = MagicMock()

    # Membuat Mock untuk cursor
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menentukan data buku palsu yang akan dikembalikan
    data_buku = [
        {
            "id_buku": 1,
            "judul": "Buku Testing",
            "penulis": "Penulis QA",
            "tahun_terbit": 2026
        }
    ]

    mock_cursor.fetchall.return_value = data_buku

    # Menjalankan fungsi get_all_buku()
    hasil = model.get_all_buku()

    # Memastikan hasil sesuai dengan data yang diharapkan
    assert hasil == data_buku

    # Memastikan query SQL dijalankan
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM buku ORDER BY id_buku ASC"
    )

    # Memastikan cursor ditutup setelah digunakan
    mock_cursor.close.assert_called_once()