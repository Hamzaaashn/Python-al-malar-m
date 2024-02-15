sayı1 = float(input("Birinci Sayıyı Girin :\n"))
sayı2 = float(input("İkinci Sayıyı Girin :\n"))

print("Toplama : + \n",
      "Çıkarma : - \n",      
      "Çarpma : * \n",
      "Bölme : / ")
işlem = input("İşlem Seçin :\n")

if işlem == "+" :
    print("Toplama Sonucu :",sayı1 + sayı2)


elif işlem == "-" :
    print("Çıkarma Sonucu :",sayı1 - sayı2)

elif işlem == "*" :
    print("Çarpma Sonucu :",sayı1 * sayı2)

elif işlem == "/" :
    print("Bölme Sonucu :",sayı1 / sayı2)