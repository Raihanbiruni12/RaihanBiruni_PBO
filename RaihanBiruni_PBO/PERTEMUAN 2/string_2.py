barang_diskon = "Kemeja"
Harga_asli = 150000
diskon_persen = 20

harga_diskon = Harga_asli * (100 - diskon_persen)/100

pesan = "Hemat hingga {:.0f}% untuk {}!\n".format(diskon_persen, barang_diskon)
pesan += "Harga Asli: Rp {:,.0f}\n".format(Harga_asli)
pesan += "Harga setelah diskon Rp {:,.0f}".format(harga_diskon)

print(pesan)