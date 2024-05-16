def hitung_gerak(kecepatan_awal, percepatan, waktu):
    """
    Fungsi untuk menghitung kecepatan akhir dan jarak tempuh dalam GLBB.

    Args:
        kecepatan_awal (float): Kecepatan awal benda (m/s).
        percepatan (float): Percepatan benda (m/s*2)
        waktu (float): Waktu (s)

    Returns:
        float: Kecepata akhir (m/s)
        float: Jarak yang di tempuh (m)
    """
    v = kecepatan_awal + percepatan * waktu
    s = kecepatan_awal * waktu + 0.5 * percepatan * waktu**2
    return v, s

#input data
data = []
while True:
    try:
        v_awal = input("Masukkan kecepatan awal (atau 'n' untuk keluar): ")
        if v_awal.lower() == 'n':
            print("Program berhenti.")
            break
        v_awal = float(v_awal)
        percepatan = float(input("Masukkan percepatan: "))
        waktu = float(input("Masukkan waktu: "))

        v_akhir, jarak = hitung_gerak(v_awal, percepatan, waktu)
        data.append((v_awal, percepatan, waktu, v_akhir, jarak))
        
    except ValueError:
        print("Input tidak valid. Silahkan coba lagi.")

# Tampilkan tabel
if data:
    print("| No | Kecepatan Awal | Percepatan | Waktu | Kecepatan Akhir | Jarak |")
    print("|----+----------------+------------+-------+-----------------+---------|")

    for i, row in enumerate(data, start=1):
        v_awal, percepatan, waktu,v_akhir, jarak = row
        print(f"| {i:2d} | {v_awal:13.2f} | {percepatan:10.2f} | {waktu:5.2f} | {v_akhir:14.2f} | {jarak:7.2f} |")

else:
    print("Tidak ada data yang diinput.")
