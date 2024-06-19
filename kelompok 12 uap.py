from termcolor import cprint
import time

print("="*63)
print("===== S E L A M A T  D A T A N G  D I  M A R T  B U K I T =====")
print("="*63)
print()
n = str(input("Kode Kasir : "))
while (n != "STAFF MART"):
    print("Kode Anda salah, silahkan input kembali")
    n = str(input("Kode Kasir : "))
while (n == "STAFF MART"):   
    print("="*63)
    print("===== M E N U   K A S I R =====")
    print("="*63)
    print()

    open_menu = input("Apakan anda ingin masuk ke menu utama? (y/n) : ")
    if open_menu == "n":
        print("keluar dari memu utama")
        break
    elif open_menu == "y":
        #Menu
        list_mart = ["1. Biskuat 8k", "2. Chimory 10k", "3. Ultra Milk 7k"]
        stok = [50, 50, 50]
        harga = 0
        struk = " "

        #Cetak Menu
        print()
        print(" "*63)
        print("========== D A F T A R  M E N U ==========")
        print(" "*63)
        for mart in list_mart:
            print(" ", mart)

        def hitung_mart(menu, A):
            global stok
            stok[int(menu)-1] = stok[int(menu)-1] - A
            if (stok[int(menu) - 1] <= 0):
                cprint("Stok tidak cukup", "black", "on_red")
                stok[int(menu) - 1] = stok[int(menu) - 1] + A
                print("Stok menu ke-{} hanya: {}".format(list_mart[int(menu)- 1]))
                return
            global struk
            if menu == "1":
                C = int(A*8000)
                ss = ("Biskuat {} x {} = {}".format(A,8000,C))
                struk = struk + ss + "\n"
            elif menu == "2":
                C = int(A*5000)
                ss = ("Chimory {} x {} = {}".format(A,10000,C))
                struk = struk + ss + "\n"
            elif menu =="3":
                C = int(A*7000)
                ss = ("Ultra Milk {} x {} = {}".format(A,7000,C))
                struk = struk + ss + "\n"
            else:
                C = 0
        
            global harga
            harga = harga + C

        #Input belanjaan
        print() 
        print("========== M E N U  P E S A N A N ==========")
        print()
        belanja_lagi = 1
        for i in range(belanja_lagi):
            cprint("Selamat berbelanja", "black", "on_blue")
            varians_belanja = int(input("masukkan varians belanjaan anda : "))
            while (varians_belanja):
                menu = input("Pilih menu (1/2/3): ")
                A = eval(input("Berapa pcs: "))
                hitung_mart(menu, A)
                varians_belanja = varians_belanja - 1
        print("-"*63)  
        #Cetak struk
        print("========== S T R U K ==========")
        print()
        print("===== M A R T  B U K I T =====")     
        pembeli = input("Customer : ")
        staff = input("Cashier : ")

        tanggal = time.asctime(time.localtime(time.time()) )
        print("Date : ", tanggal)
        print("-"*47)
        print(struk)

        total_harga = int(harga)
        print("Subtotal Rp.",format (total_harga))
        if total_harga > 200000:
            diskon = int(input("Diskon(%) : "))
            total_harga = total_harga - ((diskon/100)*total_harga)
            print("Total Rp.",format(total_harga))
        else:
            print("Total Rp. ",format(total_harga))
        bayar = int(input("Cash Rp. "))
        kembali = bayar - total_harga
        print("Kembalian Rp.", kembali)

        #Mengumpulkan data
        def data(pembeli, staff, total_harga):
            with open("data.txt",'a') as f:
                f.write(f"{pembeli}, {staff}, {total_harga}\n")
        print("data berhasil ditambahkan.\n")
        data(pembeli, staff, total_harga)