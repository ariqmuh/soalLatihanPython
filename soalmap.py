list1 = [1, 3, 4, 5]
list2 = [22, 17, 19, 20, 14]
list3 = [1, 3, 5]
list4 = [2, 4, 6]

def genapGanjil(angka):
    if (angka % 2 == 0):
        return "Genap"        
    return "Ganjil"

def ubahGenapGanjil(listAngka):
    return list(map(genapGanjil, listAngka))

list1 = ubahGenapGanjil(list1)
list2 = ubahGenapGanjil(list2)
list3 = ubahGenapGanjil(list3)
list4 = ubahGenapGanjil(list4)

print(list1)
print(list2)
print(list3)
print(list4)
