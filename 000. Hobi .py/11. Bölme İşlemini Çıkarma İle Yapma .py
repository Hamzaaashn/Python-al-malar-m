bölünen = float(input("Bölünecek Sayıyı Girin :\n"))
bölen = int(input("Bölünecek Girin :\n"))
sonuç = 0

for sayaç in range(bölen) :
    while sonuç < 0 :
        sonuç -= bölünen
sonuç += bölünen
    
print("Sonuç :\n",sonuç)