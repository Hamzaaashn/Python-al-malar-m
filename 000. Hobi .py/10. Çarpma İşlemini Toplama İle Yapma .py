çarpılan = float(input("Çarpılacak Sayıyı Girin :\n"))
çarpan = int(input("Çarpanı Girin :\n"))
sonuç = 0

for sayaç in range(1,çarpan+1) :
    sonuç += çarpılan
print("Sonuç :\n",sonuç)