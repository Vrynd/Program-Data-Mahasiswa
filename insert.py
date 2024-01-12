# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# Membuat fungsi insert
def tambahData(nama, kampus, tmpt_lahir, thn_lahir, umur):
    cursor = conn.cursor()
    query = "INSERT INTO data_mahasiswa (nama, kampus, tmpt_lahir, thn_lahir, umur) VALUES (?, ?, ?, ?, ?)"
    values = (nama, kampus, tmpt_lahir, thn_lahir, umur)
    cursor.execute(query, values)
    conn.commit()
