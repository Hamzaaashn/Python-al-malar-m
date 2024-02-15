sayı1 = int(input("Lütfen Birinci Sayıyı Buraya Girin : \n"))
sayı2 = int(input("Lütfen İkinci Sayıyı Buraya Girin : \n"))
toplam = 0

while sayı1 <= sayı2 :
    
    toplam = sayı1 + toplam
    sayı1 += 1

while sayı1 >= sayı2 :
    
    toplam = sayı1 + toplam
    sayı1 -= 1

print("Girdiğiniz 2 Sayı Arasındaki Sayıların Toplamı:\n", toplam)