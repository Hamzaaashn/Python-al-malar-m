def üçe_bölme(üçe_böl):   
    if  üçe_böl % 3 == 0:
        return üçe_böl


def beşe_bölme(beşe_böl):
    if beşe_böl % 5 == 0 :
        return beşe_böl

girilen_sayı = int(input("Sayı Girin :\n"))
sayı_üç = üçe_bölme(girilen_sayı)
sayı_beş = beşe_bölme(girilen_sayı)


if sayı_üç  and sayı_beş  :
    print("Bu Sayı 15' E Tam Bölünür")

else :
    print("Sayı 15' E Tam Bölünmez")