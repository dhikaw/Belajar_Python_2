n = str(input("Masukkan Kata : "))

def palindrom(n):
    if n == n[::-1]:
        print("Palindrom")
    else:
        print("Bukan Palindrom")
        
palindrom(n)