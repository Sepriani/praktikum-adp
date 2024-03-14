print("menghitung Rata_Rata, Ragam, Dan Simpangan Baku")
print("Menghitung Luas Dan Volume")
d1 = int(input("Masukkan data ke-1= "))
d2 = int(input("Masukkan data ke-2= "))
d3 = int(input("Masukkan data ke-3= "))
d4 = int(input("Masukkan data ke-4= "))
d5 = int(input("Masukkan data ke-5= "))
Rata_Rata = (d1 + d2 + d3 + d4 + d5)/ 5
Ragam = (d1 - Rata_Rata)**2  + (d2 - Rata_Rata)**2 + (d3 - Rata_Rata)**2 + (d4 - Rata_Rata)**2 + (d5 - Rata_Rata)**2 / 5
Simpang_Baku = (Ragam)**1/2
print("Rata_Rata Data Adalah = ", Rata_Rata)
print("Ragam Data Adalah = ", Ragam)
print("Simpang_Baku Data Adalah = ", Simpang_Baku)
