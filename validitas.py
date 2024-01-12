# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# Membuat fungsi validitas tipe data yang diinputkan
def validitasData(nama, kampus, tmpt_lahir, thn_lahir, umur):
    if not all(map(str.isalpha, nama.split())):
        print("Nama harus terdiri dari huruf saja!")
        return False
    if not all(map(str.isalpha, kampus.split())):
        print("Nama Kampus harus terdiri dari huruf saja!")
        return False
    if not all(map(str.isalpha, tmpt_lahir.split())):
        print("Tempat Lahir harus terdiri dari huruf saja!")
        return False
    if not thn_lahir.isdigit() or len(thn_lahir) != 4:
        print("Tahun Lahir harus berupa angka 4 digit!")
        return False
    try:
        umur = int(umur)
        if umur < 0:
            print("Umur harus merupakan bilangan bulat positif")
            return False
        return True
    except ValueError:
        print("Umur harus berupa bilangan bulat")
        return False