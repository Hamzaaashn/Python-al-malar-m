toplam = 0

sayı1 = int(input("Birinci Sayıyı Girin :\n"))
sayı2 = int(input("İkinci Sayıyı Girin :\n"))

for sayı in range(sayı1,sayı2) :
    toplam += sayı

print("Girdiğiniz İki Sayı Arasındaki Sayıların Toplamı :\n",toplam)