import random

print("=== Sayı Tahmin Oyunu ===")
print("1 ile 100 arasında bir sayı tuttum. 3 tahmin hakkın var!")

sayi = random.randint(1, 100)
hak = 3

while hak > 0:
    tahmin = int(input("Tahminin: "))

    if tahmin == sayi:
        print(":) Tebrikler! Doğru bildin!")
        break
    elif tahmin < sayi:
        print("Yukarı çık!")
    else:
        print("Aşağı in!")

    hak -= 1
    print("Kalan hakkın:", hak)

if hak == 0:
    print(":( Tahmin hakkın bitti! Tutulan sayı:", sayi)
