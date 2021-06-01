import math
jmlHari = 485
sisaHari = jmlHari

# 485 / 360 untuk dapat tahun
tahun = math.floor(sisaHari/360)

# 485 % 360 
sisaHari %= 360

# bulan 125 / 30 
bulan = math.floor(sisaHari/30)

# 125 % 30 
sisaHari %= 30

# minggu 5 / 7
minggu = math.floor(sisaHari/7)

# 5 % 7
sisaHari %= 7

# print
print(str(jmlHari) + " Hari adalah")
print('{} Tahun'.format(int(tahun)))
print('{} Bulan'.format(int(bulan)))
print("{} Minggu".format(int(minggu)))
print ("{} Hari".format(sisaHari))


