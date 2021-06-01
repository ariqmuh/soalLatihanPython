listGaji = [9100000, 9800000, 9500000, 10300000, 9300000]

def ubahGaji(listAngka):
    return list(filter(lambda gaji : gaji * 95/100 > 9000000, listAngka))

listGaji = ubahGaji(listGaji)
print(listGaji)