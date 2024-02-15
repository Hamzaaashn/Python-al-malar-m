sınav1 = float(input("Lütfen Birinci Sınav Notunuzu Girin :\n"))
sınav2 = float(input("Lütfen İkinci Sınav Notunuzu Girin :\n"))
performans = float(input("Lütfen Performans Notunuzu Girin :\n"))

if (sınav1 +sınav2 + performans) / 3 >= 50 :
    print("Başarılı")
else:
    print("Başarısız")