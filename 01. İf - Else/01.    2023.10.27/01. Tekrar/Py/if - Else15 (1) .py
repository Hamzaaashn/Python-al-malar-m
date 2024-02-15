sinema=15
tiyatro=10

print("İzlemek İstediğinizi Seçin")
seçim=input("Tiyatro "
            "-"
            "Sinema\n")

print("Öğrenim Durumunuzu Girin")
öğrenim_durumu=input("Öğrenci "
                     "-"
                     "Normal\n")
 
if seçim == "Tiyatro" and öğrenim_durumu == "Öğrenci":
    print("Ücret :\n", 10/2)
elif seçim == "Tiyatro" and öğrenim_durumu == "Normal":
    print("Ücret :\n", 10)
elif seçim == "Sinema" and öğrenim_durumu == "Normal":
    print("Ücret :\n", 15)
elif seçim == "Sinema" and öğrenim_durumu == "Öğrenci":
    print("Ücret :\n", 15/2)