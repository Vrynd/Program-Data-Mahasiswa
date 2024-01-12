# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# Membuat fungsi tabel
def buatTabel():
    cursor = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS data_mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama VARCHAR(50),
            kampus VARCHAR(50),
            tmpt_lahir VARCHAR(50),
            thn_lahir INTEGER(11),
            umur INTEGER(5)
        )"""

    cursor.execute(sql)
    conn.commit()
    print("Database dan Tabel Berhasil Dibuat")
buatTabel()
