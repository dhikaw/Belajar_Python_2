n = int(input("Masukkan Angka : "))

def bilangan_prima(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

print(bilangan_prima(n))