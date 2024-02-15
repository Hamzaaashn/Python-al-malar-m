sınav1 = float(input("Birinci Sınav Notunuzu Girin :\n"))
sınav2 = float(input("İkinci Sınav Notunuzu Girin :\n"))
performans = float(input("Performans Notunuzu Girin :\n"))

if (sınav1 + sınav2 + performans)  / 3 >= 50:
    print("Başarılı")

else:
    print("Başarısız")