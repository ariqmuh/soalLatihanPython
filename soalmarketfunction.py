daftarBuah = [
    ["Apel", 20, 10000],
    ["Jeruk", 15, 15000], 
    ["Anggur", 25, 20000]
]

cart = []

def menampilkanDaftarBuah():
    print("Daftar Buah \n")
    print('Index\t| Nama  \t| Stock\t| Harga')
    for i in range(len(daftarBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,daftarBuah[i][0],daftarBuah[i][1],daftarBuah[i][2]))

def menambahDaftarBuah():
    menampilkanDaftarBuah
    namaBaru = str(input("Masukkan Nama Buah : "))
    stockBaru = int(input("Masukkan Stock Buah : "))
    hargaBaru = int(input("Masukkan Harga Buah : "))
    daftarBuah.append([namaBaru, stockBaru, hargaBaru])
    menampilkanDaftarBuah

def menghapusBuah():
    menampilkanDaftarBuah
    hapus = int(input("Masukkan index buah yang ingin dihapus : "))
    del daftarBuah[hapus]
    menampilkanDaftarBuah

def membeliBuah():
    menampilkanDaftarBuah
    while (True):
        pilihIndex = int(input("Masukkan index buah yang ingin dibeli : "))
        pilihJumlah = int(input("Masukkan jumlah yang ingin dibeli : "))
        if (pilihJumlah > daftarBuah[pilihIndex][1]):
            print("Stock tidak cukup, stock {} tinggal {}".format(daftarBuah[pilihIndex][0], daftarBuah[pilihIndex][1]))
        else:
             cart.append([daftarBuah[pilihIndex][0], pilihJumlah, daftarBuah[pilihIndex][2], pilihIndex])
        print("Isi Cart : \n")
        print("Nama  \t| Qty\t| Harga")
        for item in cart:
            print("{}  \t| {}\t| {}".format(item[0], item[1], item[2]))
        checker = input("Mau beli yang lain? (ya/tidak) = ")
        if (checker == 'tidak'):
            break
    print('Daftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    totalHarga = 0
    for item in cart:
        print("{}\t| {}\t| {}\t| {}".format(item[0], item[1], item[2], item[1]*item[2]))
        totalHarga += item[1]*item[2]
    while (True):
        print("Total yang harus dibayar = {}".format(totalHarga))
        jumlahUang = int(input("Masukkan jumlah uang : "))
        if (jumlahUang > totalHarga):
            kembali = jumlahUang - totalHarga
            print("Terima kasih\n \n Uang kembali anda : {}".format(kembali))
            for item in cart:
                daftarBuah[item[3]][1] -= item[1]
            del cart[:]
            break
        elif (jumlahUang == totalHarga):
            print("Terima kasih")
            for item in cart:
                daftarBuah[item[3]][1] -= item[1]
            del cart[:]
            break
        else:
            kekurangan = totalHarga - jumlahUang
            print("Uang anda kurang sebesar : {}".format(kekurangan))

print("Selamat Datang di Pasar Buah \n")
print('''
List Menu : 
1. Menampilkan Daftar Buah
2. Menambah Buah
3, Menghapus Buah
4. Membeli Buah
5. Exit Program
''')

while (True):
    menu = int(input("Masukkan angka menu yang ingin dijalankan : "))
    if menu == 1:
        menampilkanDaftarBuah()
    elif menu == 2:
        menambahDaftarBuah()
    elif menu == 3:
        menghapusBuah()
    elif menu == 4:
        membeliBuah()
    elif menu == 5:
        break
    else:
        menu
    



