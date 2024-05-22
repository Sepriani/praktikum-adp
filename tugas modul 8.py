import os
import datetime

def manajemen_keuangan():
    #membuat dictionary untuk menyimpan data keuangan
    data_keuangan = {}

    # Membaca data keuangan dari file jika ada keuangan
    if os.path.isfile("data_keuangan.txt"):
        with open("data_keuangan.txt","r") as file:
            for line in file:
                tanggal, keterangan, jumlah, tipe = line.strip().split(",")
                data_keuangan[(tanggal, keterangan, float(jumlah), tipe)] = True


    # Membuat menu untuk pengguna
    menu = {
        "1": "Simpan Data",
        "2": "Hapus Data",
        "3": "Tampilkan Data",
        "4": "Kembali ke Menu Awal"
    }

    while True:
        print("Selamat datang di manajemen keuangan!")
        print("Silahkan Pilih opsi yang Anda Inginkan: ")
        for key, value in menu.items():
            print(f"{key}. {value}")

        pilihan = input("Masukkan nomor pilihan Anda: ")

        if pilihan == "1":
            simpan_data(data_keuangan)
        elif pilihan == "2":
            hapus_data(data_keuangan)
        elif pilihan == "3":
            tampilkan_data(data_keuangan)
        elif pilihan == "4":
            print("Terimakasih telah menggunakan manajemen keuangan! ")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")


def simpan_data(data_keuangan):
    tanggal = datetime.date.today().strftime("%Y-%m-%d")
    keterangan = input("Masukkan keterangan transaksi: ")
    jumlah = float(input("Masukkan jumalah transaksi: "))
    tipe = input("Masukkan tipe transaksi(pemasukan/pengeluaran): ")


    data_keuangan[(tanggal, keterangan, jumlah, tipe)] = True

    with open("data_keuangan.txt", "a") as file:
        file.write(f"{tanggal},{keterangan},{jumlah}, {tipe}\n")

    print("Data berhasil disimpan.")

def hapus_data(data_keuangan):
    tanggal = input("Masukkan tanggal transaksi (%Y-%m-%d): ")
    keterangan = input ("Masukkan keterangan transaksi: ")
    jumlah = float(input("Masukkan jumlah transaksi: "))
    tipe = input("Masukkan tipe transaksi (pemasukan/pengeluaran): ")

    key = (tanggal, keterangan, jumlah, tipe)
    if key in data_keuangan:
        del data_keuangan[key]
        with open("data_keuangan.txt","w") as file:
            for data in data_keuangan:
                file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
        print("Data berhasil dihapus.")
    else:
            print("Data tidak ditemukan.")

def tampilkan_data(data_keuangan):
    if not data_keuangan:
        print("Tidak ada data keuangan yang tersimpan.")
    else:
        print("Data keuangan:")
        print("Tanggal\t\tKeterangan\t\tJumlah\t\tTipe")
        print("_" * 80)
        for tanggal, keterangan, jumlah, tipe in sorted(data_keuangan):
            print(f"{tanggal}\t{keterangan}\t{jumlah:.2f}\t{tipe}")

if __name__ == "__main__":
    manajemen_keuangan()

