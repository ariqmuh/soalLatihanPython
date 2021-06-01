daftarBuah = [
    {
        'nama' : 'Apel',
        'stock' : 20,
        'harga' : 1000
    },
    {
        'nama' : 'Jeruk',
        'stock' : 15,
        'harga' : 15000
    },
    {
        'nama' : 'Anggur',
        'stock' : 25,
        'harga' : 20000
    }
]
cart = []

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
        print("Daftar Buah \n")
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(daftarBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,daftarBuah[i]['nama'],daftarBuah[i]['stock'],daftarBuah[i]['harga']))
    elif menu == 2:
        namaBaru = str(input("Masukkan Nama Buah : "))
        stockBaru = int(input("Masukkan Stock Buah : "))
        hargaBaru = int(input("Masukkan Harga Buah : "))
        daftarBuah.append({
            'nama' : namaBaru, 
            'stock' : stockBaru, 
            'harga' : hargaBaru
        })
        print("Daftar Buah \n")
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(daftarBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,daftarBuah[i]['nama'],daftarBuah[i]['stock'],daftarBuah[i]['harga']))
    elif menu == 3:
        hapus = int(input("Masukkan index buah yang ingin dihapus : "))
        del daftarBuah[hapus]
        print("Daftar Buah \n")
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(daftarBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,daftarBuah[i]['nama'],daftarBuah[i]['stock'],daftarBuah[i]['harga']))
    elif menu == 4:
        print("Daftar Buah \n")
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(daftarBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,daftarBuah[i]['nama'],daftarBuah[i]['stock'],daftarBuah[i]['harga']))
        while (True):
            pilihIndex = int(input("Masukkan index buah yang ingin dibeli : "))
            pilihJumlah = int(input("Masukkan jumlah yang ingin dibeli : "))
            if (pilihJumlah > daftarBuah[pilihIndex]['stock']):
                print("Stock tidak cukup, stock {} tinggal {}".format(daftarBuah[pilihIndex]['nama'], daftarBuah[pilihIndex]['stock']))
            else:
                cart.append({
                    'nama' : daftarBuah[pilihIndex]['nama'],
                    'qty' : pilihJumlah, 
                    'harga' : daftarBuah[pilihIndex]['harga'],
                    'index' : pilihIndex
                    })
            print("Isi Cart : \n")
            print("Nama \t| Qty\t| Harga")
            for item in cart:
                print("{} \t| {}\t| {}".format(item['nama'], item['qty'], item['harga']))
            checker = input("Mau beli yang lain? (ya/tidak) = ")
            if (checker == 'tidak'):
                break
        print('Daftar Belanja :')
        print('Nama\t| Qty\t| Harga\t| Total Harga')
        totalHarga = 0
        for item in cart:
            print("{}\t| {}\t| {}\t| {}".format(item['nama'], item['qty'], item['harga'], item['qty']*item['harga']))
            totalHarga += item['qty']*item['harga']
        while (True):
            print("Total yang harus dibayar = {}".format(totalHarga))
            jumlahUang = int(input("Masukkan jumlah uang : "))
            if (jumlahUang > totalHarga):
                kembali = jumlahUang - totalHarga
                print("Terima kasih\n \n Uang kembali anda : {}".format(kembali))
                for item in cart:
                    daftarBuah[item['index']]['stock'] -= item['qty']
                cart.clear()
                break
            elif (jumlahUang == totalHarga):
                print("Terima kasih")
                for item in cart:
                    daftarBuah[item['index']]['stock'] -= item['qty']
                del cart[:]
                break
            else:
                kekurangan = totalHarga - jumlahUang
                print("Uang anda kurang sebesar : {}".format(kekurangan))
    elif menu == 5:
        break
    else:
        menu
    
