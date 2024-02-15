def hafta_bilgisi_alma() :
    hafta_bilgisi = int(input("Kaç Hafta Boyunca Derse Girdin ? :\n"))
    
    return hafta_bilgisi
hafta_bilgisi = hafta_bilgisi_alma()   



def saat_bilgisi_alma(hafta_bilgisi):
    toplam=0
    for i in range(hafta_bilgisi) :
       saat_bilgisi=float(input(str(i+1)+". hafta kaç saat derse girdin:"))
       toplam+= saat_bilgisi
    return toplam
toplam=saat_bilgisi_alma(hafta_bilgisi)
    



def yazdırma(toplam):
    
    print("Eğer Toplam Saatleri Öğrenmek İstiyorsan :\n","Toplam (T)\n","Eğer Ortalama Saatleri Öğrenmek İstiyorsan :\n","Ortalama (O)")
    toplam_veya_ortalama = input(": ")

    if toplam_veya_ortalama == "T" or toplam_veya_ortalama == "t" :
     print("Toplam Ders Süresi :\n",toplam)

    elif toplam_veya_ortalama == "O" or toplam_veya_ortalama == "o" :
     print("Hafta Başına Düşen Ortalama Ders Süresi :\n",toplam / hafta_bilgisi)



yazdırma(toplam)