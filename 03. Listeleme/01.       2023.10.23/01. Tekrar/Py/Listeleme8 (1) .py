ders = ["B","İ","L","İ","Ş","İ","M"]
dersA = ders.copy()
dersB = ders.copy()
dersC = ders.copy()
dersÇ = ders.copy()
dersD = ders.copy()
dersE = ders.copy()
dersF = ders.copy()





print(ders)

print()
print()

#A#

dersA.sort()
print("Listenin Alfabetik Sıralanışı :\n",dersA)

print()
print()
print()

#B#

dersB.reverse()
print("Listenin Tersten Yazımı :\n",dersB)

print()
print()
print()

#C#

dersC_sayı = dersC.count("İ")
print("Listenin İçinde " ,dersC_sayı,"Tane İ Sayısı Var")

print()
print()
print()

#Ç#

del dersÇ[4]
del dersÇ[4]
print("Listenin",dersÇ ,"Şeklinde Yazımı")

print()
print()
print()


#D#

alan_listesi = dersD.copy()
print("Listenin Kopyalanmış Hali :\n",alan_listesi)

print()
print()
print()



#E#

dersE.clear()
print("Boş Liste :\n",dersE)
print()
print()
print()


#F#

print( "L Harfinin Listedeki Konumu :\n",dersF.index("L"))
