sayı1 = float(input("İlk Sayıyı Girin :\n"))
sayı2 = float(input("İkinci Sayıyı Girin :\n"))
toplam = 0
if sayı1 < sayı2 :
    while sayı1 != sayı2:
        toplam += sayı1
        sayı1 += 1
    print(toplam + sayı2)

else:
    while sayı2 != sayı1:
        toplam += sayı2
        sayı2 += 1
    print(toplam + sayı1)