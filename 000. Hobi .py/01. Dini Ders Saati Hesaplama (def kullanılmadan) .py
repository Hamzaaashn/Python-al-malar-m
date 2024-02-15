hafta_bilgisi = int(input("Kaç Hafta Boyunca Derse Girdin ? :\n"))

sayaç = 1
toplam = 0


for saat_bilgisi in range(hafta_bilgisi) :

    print(sayaç,". Hafta Kaç Saat Derse Girdin ?")
    saat_bilgisi = float(input(": "))
    toplam += saat_bilgisi
    sayaç += 1


print("Eğer Toplam Saatleri Öğrenmek İstiyorsan :\n","Toplam (T)\n","Eğer Ortalama Saatleri Öğrenmek İstiyorsan :\n","Ortalama (O)")
toplam_veya_ortalama = input(": ")

if toplam_veya_ortalama == "T" or toplam_veya_ortalama == "t"or toplam_veya_ortalama == "Toplam" or toplam_veya_ortalama == "toplam":
    print("Toplam Ders Süresi :\n",toplam)

elif toplam_veya_ortalama == "O" or toplam_veya_ortalama == "o" or toplam_veya_ortalama == "Ortalama" or toplam_veya_ortalama == "ortalama":
    print("Hafta Başına Düşen Ortalama Ders Süresi :\n",toplam / hafta_bilgisi)