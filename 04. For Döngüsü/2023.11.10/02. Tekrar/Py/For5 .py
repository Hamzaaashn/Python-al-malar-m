sayı1 = int(input("Baştaki Sayıyı Girin :\n"))
sayı2 = int(input("Sondaki Sayıyı Girin :\n"))
sayılar = range(sayı1,sayı2)
print()
print()
print()

toplam = 0

for sayı in sayılar:
    
    toplam += sayı
    
print(sayı1,"İle",sayı2,"Arasındaki Sayıların Toplamı :\n",toplam)