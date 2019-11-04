num = int(input("Masukan Nilai  N:"))

from random import random
a = random()

jumlah = num+1
start = 0
stop = jumlah
step = 1
for i in range ( start, stop, step):
    print("Data Ke:", i, "->", (a))
print("Selesai")
