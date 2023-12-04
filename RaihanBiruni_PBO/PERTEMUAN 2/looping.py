# Daftar barang dan harganya
daftar_barang = {
    "Buku": 15000,
    "Pensil": 2000,
    "Kertas": 5000,
    "Penghapus": 3000,
    "Spidol": 7000
}

# Inisialisasi keranjang belanja
keranjang = {}

# Input dari pengguna untuk memilih barang
while True:
    print("\nDaftar Barang yang Tersedia:")
    for barang, harga in daftar_barang.items():
        print(f"{barang}: Rp {harga:,.0f}")
    
    pilihan = input("\nPilih barang yang ingin dibeli (Ketik 'selesai' untuk mengakhiri belanja): ")
    
    if pilihan.lower() == "selesai":
        break
    
    if pilihan in daftar_barang:
        jumlah = int(input(f"Jumlah {pilihan} yang ingin dibeli: "))
        if pilihan in keranjang:
            keranjang[pilihan] += jumlah
        else:
            keranjang[pilihan] = jumlah
    else:
        print("Barang tidak valid. Silakan pilih barang yang tersedia.")

# Menampilkan rincian belanja
print("\nRincian Belanja:")
total_harga = 0
for barang, jumlah in keranjang.items():
    harga_barang = daftar_barang[barang]
    total_barang = harga_barang * jumlah
    total_harga += total_barang
    print(f"{barang} ({jumlah} buah): Rp {total_barang:,.0f}")

# Menampilkan total harga
print(f"Total harga belanja: Rp {total_harga:,.0f}")

# Terima kasih
print("\nTerima kasih telah berbelanja!")