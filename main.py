# Program Utama
# Created by - Rifky Verryan Dhika
# Universitas Teknologi Yogyakarta - 2023

# Mengimpor Module
import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')
import os
from insert import tambahData
from select_all import tampilkanData
from update import perbaruiData
from delete import hapusData
from validitas import validitasData

# Membuat menu program
while True:
    print("\nPROGRAM INPUT DATA MAHASISWA 2024 : ")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Perbarui Data")
    print("4. Hapus Data")
    print("x. Keluar")
    pilih_menu = input("Massukan Operasi [1/2/3/4/x] >> ")

    os.system('cls')
    if pilih_menu == "1":
        count = 0
        while True:
            cursor = conn.cursor()
            nama = input("Massukan Nama : ")
            kampus = input("Massukan Nama Kampus : ")
            tmpt_lahir = input("Massukan Tempat Lahir : ")
            thn_lahir = input("Massukan Tahun Lahir (YYYY) : ")
            umur = input("Massukan Umur : ")
            count += 1
            if validitasData(nama, kampus, tmpt_lahir, thn_lahir, umur ):
                tambahData(nama, kampus, tmpt_lahir, thn_lahir, umur)
            os.system('cls')
            coba_lagi = input("> Tambah data lagi [Y/T] : ")
            if coba_lagi != 'y' and coba_lagi != 'Y':
                print("{} Data Berhasil Disimpan".format(count))
                break
    elif pilih_menu == "2":
        tampilkanData()
    elif pilih_menu == "3":
        count = 0
        while True:
            cursor = conn.cursor()
            tampilkanData()
            id = input("Pilih id yang ingin diubah : ")
            cursor.execute("SELECT * FROM data_mahasiswa WHERE id="+id)
            result = cursor.fetchall()
            count += 1
            for value in result:
                nama = input("Massukan Nama : "+value[1]+ " -> ") or value[1]
                kampus = input("Massukan Nama Kampus : "+value[2]+ " -> ") or value[2]
                tempat_lahir = input("Massukan Tempat Lahir : "+value[3]+ " -> ") or value [3]
                tahun_lahir = input("Massukan Tahun Lahir (YYYY) : "+str(value[4])+ " -> ") or str(value[4])
                usia = input("Massukan Usia : "+str(value[5])+ " -> ") or str(value[5])
            if validitasData(nama, kampus, tempat_lahir, tahun_lahir, int(usia)):
                perbaruiData(int(id), nama, kampus, tempat_lahir, tahun_lahir, int(usia))
            os.system('cls')
            coba_lagi = input("> Perbarui data lagi [Y/T] :")
            if coba_lagi != 'y' and coba_lagi != 'Y':
                print("{} Data Berhasil Diperbarui".format(count))
                break
    elif pilih_menu == "4":
        count = 0
        while True:
            cursor = conn.cursor()
            tampilkanData()
            id = int(input("Pilih id yang ingin dihapus : "))
            yakin = input("> Yakin ingin menghapus data ini [Y/T] : ")
            if yakin == 'y' or yakin == 'Y':
                hapusData(id)
            else:
                print("*Penghapusan data dibatalkan")
            count += 1
            os.system('cls')
            hapus = input("> Hapus data lagi [Y/T] : ")
            if hapus != 'y' or hapus != 'Y':
                print("{} Data Berhasil Dihapus".format(count))
                break
    elif pilih_menu == "x":
        print("Anda Keluar Dari Menu, Program Selesai!")
        exit()
    else:
        os.system('cls')
        coba_lagi = input("> Pilihan Tidah Valid, Pilih Menu Lagi [Y/T] : ")
        if coba_lagi == 't' or coba_lagi == 'T':
            break