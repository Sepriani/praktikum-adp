print("===========================")
print("|NAMA  : SEPRIANI         |")
print("|NIM   : 2310432017       |")
print("|SHIFT : SHIFT-4          |")
print("|TUGAS : MODUL 2 PRAK ADP |")      
print("===========================")


print("-----------------------------------------------------------------")
print("|###############################################################|")
print("-----------------------------------------------------------------")

print("=================================================================")
print("|||||||||||||||||PROGRAM PEMBELIAN TIKET PESAWAT|||||||||||||||||")
print("=================================================================")

print("PROGRAM PEMBELIAN TIKET PESAWAT")
print("tujuan    | ekonomi      | bisnis        | first_class     ")
print("#---------------------------------------------------------#")
print("JAKARTA   | 1000.0       | 2000.0        | 3000.0          ")                     
print("BALI      | 1000.0       | 2000.0        | 3000.0          ")                                 
print("PADANG    | 1000.0       | 2000.0        | 3000.0          ")                               
print("JACEH     | 1000.0       | 2000.0        | 3000.0          ")                                                      
print("#---------------------------------------------------------#")


nama = input("Masukkan nama= ")
umur = int(input("Masukkan umur= "))
jenis_kelamin = input("Masukkan jenis kelamin= ")

print("Pilih tujuan keberangkatan (jakarta,bali, padang, aceh)= ")
kota_tujuan = input()
print("Pilih jenis maskapai (ekonomi, bisnis, first class)= ")
jenis_maskapai = input()
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin di beli= "))

if jenis_maskapai =="ekonomi":
    harga_tiket = 1000.0
elif jenis_maskapai =="bisnis":
    harga_tiket = 2000.0
elif jenis_maskapai =="first class":
    harga_tiket = 3000.0
else:
    harga_tiket = 0

total_harga = harga_tiket * jumlah_tiket 

if jumlah_tiket > 3:
    diskon = 0.25 * total_harga
    total_harga -= diskon
else:
    diskon = 0

total_harga = harga_tiket * jumlah_tiket - diskon

print("\n\n======================== Struk Pemesanan ========================")
print("Nama= ",nama)
print("Umur= ",umur)
print("Jenis Kelamin= ",jenis_kelamin)
print("Kota Tujuan= ",kota_tujuan)
print("Jenis Maskapai= ",jenis_maskapai)
print("Jumlah Tiket= ",jumlah_tiket)
print("Total Harga= $",format(total_harga, ".2f"))
