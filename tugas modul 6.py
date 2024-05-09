print("menentukan nama barang dan keuntungannya")

jumlah_barang = int(input("masukkan jumlah barang: "))

barang =[ ]

for i in range(jumlah_barang):
    nama = input(f"masukkan nama barang {i+1}: ")
    harga_beli = float(input(f"masukkan harga beli barang {i+1}: "))
    harga_jual = float(input(f"masukkan harga jual barang {i+1}: "))
    jumlah_persediaan = int(input(f"masukkan jumlah persediaan barang {i+1}: "))
    barang.append([nama,harga_beli,harga_jual,jumlah_persediaan])

total_keuntungan = 0 
barang_keuntungan_terbesar = ""
barang_keuntungan_terkecil = ""


for nama, harga_beli,harga_jual, jumlah_persediaan in barang:
        keuntungan_per_barang = jumlah_persediaan * (harga_jual - harga_beli)
        total_keuntungan += keuntungan_per_barang
        
        if barang_keuntungan_terbesar == "" or keuntungan_per_barang > total_keuntungan:     
            barang_keuntungan_terbesar = nama

        if barang_keuntungan_terkecil == "" or keuntungan_per_barang < total_keuntungan:            
            barang_keuntungan_terkecil = nama

 
print("daftar barang: ")

num_rows = int(input("masukkan jumlah baris: "))
num_cols = int(input("masukkan jumlah kolom: "))
table = []

for i in range(num_rows):
    row = []
    for j in range(num_cols):   
        value = input(f"masukkan nilai baris {i+1},kolom {j+1}: ")   
        row.append(value)   
    table.append(row)
    
print()

for row in table: 
    print(" | ".join(row))
    print("-" * (len(" | ".join(row))))
    
print()
        
print(f"total keuntungan: {total_keuntungan}")
print(f"barang dengan keuntungan terbesar:{barang_keuntungan_terbesar}")
print(f"barang dengan keuntungan terkecil:{barang_keuntungan_terkecil}")
