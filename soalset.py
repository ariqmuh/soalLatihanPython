setFilmKesukaanKu = set(input('Masukkan 5 film kesukaan anda dipisahkan dengan koma : '.split(",")))
setFilmKesukaanTeman = set(input('Masukkan 5 film kesukaan teman anda dipisahkan dengan koma : '.split(",")))

setFilmYangSama = setFilmKesukaanKu.intersection(setFilmKesukaanTeman)

print("Kesukaan film kalian yang sama sebesar {}%".format((len(setFilmYangSama)/len(setFilmKesukaanKu)) * 100))