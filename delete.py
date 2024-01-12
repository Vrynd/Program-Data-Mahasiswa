# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# Membuat fungsi delete
def hapusData(id):
    cursor = conn.cursor()
    query = "DELETE FROM data_mahasiswa WHERE id = ?"
    values = (id,)
    cursor.execute(query, values)
    conn.commit()
   