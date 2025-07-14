n = int(input("Masukkan Angkan Fibbonaci = "))

def fibbonaci(n):
    if n <= 1:
        return n
    else: 
        return fibbonaci(n - 1) + fibbonaci(n - 2)

for i in range(n):
    print(fibbonaci(i))



