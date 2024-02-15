 
sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
deger = 1
for s in range(sayi):
    deger = deger * (s+1)
 
print("Faktoriyel : ", deger)