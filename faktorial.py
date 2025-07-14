n = int(input("Masukkan Angka faktorial  : "))

def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

print(faktorial(n))