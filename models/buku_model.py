from config.database import Database


class bukumodel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        """Mengambil seluruh data buku dari database."""
        if not self.conn:
            return []

        cursor = None

        try:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name} ORDER BY id_buku ASC"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data buku: {e}")
            return []

        finally:
            if cursor:
                cursor.close()

    def create_buku(self, judul, penulis, tahun_terbit):
        """Menambahkan data buku baru."""
        if not self.conn:
            return False

        cursor = None

        try:
            cursor = self.conn.cursor()

            query = f"""
                INSERT INTO {self.table_name}
                (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (judul, penulis, tahun_terbit)
            )

            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print(f"Gagal menambahkan buku: {e}")
            return False

        finally:
            if cursor:
                cursor.close()

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        """Memperbarui data buku berdasarkan ID."""
        if not self.conn:
            return False

        cursor = None

        try:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """

            cursor.execute(
                query,
                (judul, penulis, tahun_terbit, id_buku)
            )

            berhasil = cursor.rowcount > 0
            self.conn.commit()
            return berhasil

        except Exception as e:
            self.conn.rollback()
            print(f"Gagal memperbarui buku: {e}")
            return False

        finally:
            if cursor:
                cursor.close()

    def delete_buku(self, id_buku):
        """Menghapus data buku berdasarkan ID."""
        if not self.conn:
            return False

        cursor = None

        try:
            cursor = self.conn.cursor()

            query = f"""
                DELETE FROM {self.table_name}
                WHERE id_buku = %s
            """

            cursor.execute(query, (id_buku,))

            berhasil = cursor.rowcount > 0
            self.conn.commit()
            return berhasil

        except Exception as e:
            self.conn.rollback()
            print(f"Gagal menghapus buku: {e}")
            return False

        finally:
            if cursor:
                cursor.close()