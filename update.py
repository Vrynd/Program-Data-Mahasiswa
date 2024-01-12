# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# Membuat fungsi update
def perbaruiData(id, nama, kampus, tmpt_lahir, thn_lahir, umur):
    cursor = conn.cursor()
    query = "UPDATE data_mahasiswa SET nama = ?, kampus = ?, tmpt_lahir = ?, thn_lahir = ?, umur = ? WHERE id = ?"
    values = (nama, kampus, tmpt_lahir, thn_lahir, umur, id)
    cursor.execute(query, values)
    conn.commit()