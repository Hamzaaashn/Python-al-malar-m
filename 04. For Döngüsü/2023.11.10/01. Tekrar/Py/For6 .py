toplam = 0
ortalama = 0
sayaç = 0

sayı1 = int(input("Birinci Sayıyı Girin :\n"))
sayı2 = int(input("İkinci Sayıyı Girin :\n"))

for sayı in range(sayı1,sayı2) :
    toplam += sayı
    sayaç += 1
    ortalama = toplam / sayaç

print("Girdiğiniz İki Sayı Arasındaki Sayıların Ortalaması :\n",ortalama)