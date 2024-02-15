sayı1 = float(input(" Birinci Sayıyı Girin :\n"))
sayı2 = float(input(" İkinci Sayıyı Girin :\n"))
sayı3 = float(input(" Üçüncü Sayıyı Girin :\n"))

if sayı1 > sayı2 and sayı1 > sayı3 :
    print("En Büyük Sayı Birinci Sayı :",sayı1)

elif sayı2 > sayı1 and sayı2 > sayı3 :
    print("En Büyük Sayı İkinci Sayı :",sayı2)

else:
    print("En Büyük Sayı Üçüncü Sayı :",sayı3)