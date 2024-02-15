toplam = 0
sayı = 0
ortalama = 0
sayaç = 0


while sayı != 1 :
 

 sayı = float(input("Sayıyı Girin :\n"))
 toplam += sayı
 sayaç += 1
 
sayaç -= 1
toplam -= 1
ortalama = toplam / sayaç

   
print(sayaç ,"Sayı Girdiniz Ve Girdiğiniz Sayıların Ortalaması :\n",ortalama)