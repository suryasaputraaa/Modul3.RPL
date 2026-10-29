from unittest.mock import MagicMock
from models.user_model import UserModel


def test_hash_password_konsisten():
    password_asli = "admin123"
    hash_1 = UserModel.hash_password(password_asli)
    hash_2 = UserModel.hash_password(password_asli)

    # Memastikan hasil hash tidak sama dengan plain text dan bersifat konsisten
    assert hash_1 != password_asli
    assert hash_1 == hash_2
    assert len(hash_1) == 64  # Panjang karakter standar SHA-256


def test_autentikasi_pengguna_berhasil():
    model = UserModel()
    model.conn = MagicMock()
    mock_cursor = MagicMock()

    # Simulasi kembalian data dari database ketika username & password cocok
    mock_cursor.fetchone.return_value = {
        "id_user": 1,
        "username": "petugas",
        "role": "admin"
    }
    model.conn.cursor.return_value = mock_cursor

    hasil = model.autentikasi("petugas", "admin123")

    assert hasil is not None
    assert hasil["username"] == "petugas"
    assert hasil["role"] == "admin"


def test_register_user_menyimpan_password_ter_hash():
    model = UserModel()
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    hasil = model.register_user("userbaru", "rahasia123", "anggota")

    assert hasil is True
    # Argumen kedua execute adalah (username, password_hash, role)
    params = mock_cursor.execute.call_args[0][1]
    assert params[1] != "rahasia123"
    assert params[1] == UserModel.hash_password("rahasia123")
    model.conn.commit.assert_called_once()


def test_register_user_role_tidak_valid_ditolak():
    model = UserModel()
    model.conn = MagicMock()

    hasil = model.register_user("userbaru", "rahasia123", "superadmin")

    assert hasil is False
    model.conn.cursor.assert_not_called()