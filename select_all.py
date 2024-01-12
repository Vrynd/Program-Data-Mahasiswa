# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# Membuat fungsi select
def tampilkanData():
    cursor = conn.cursor()
    query = "SELECT * FROM data_mahasiswa"
    cursor.execute(query)
    result = cursor.fetchall()

    # Membuat format tabel dalam python
    print("BIODATA MAHASISWA 2024")
    print("="*100)
    print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "Nama", "Kampus", "Tempat Lahir", "Tahun Lahir", "Umur"))
    print("-"*100)
    for data in result:
        print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}". format(data[0], data[1], data[2], data[3], data[4], data[5]))
    print("="*100)
    if len(result) == 0:
        print("*Tidak ada Data Mahasiswa")