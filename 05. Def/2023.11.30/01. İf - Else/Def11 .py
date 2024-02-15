def eşkenar(x,y,z) :
    toplam = x + y + z

    return x == 60 and y == 60 and z == 60 and toplam == 180 



def İkizkenar(x,y,z) :
    toplam = x + y + z

    return x == y or x == z or y == z and toplam == 180  



def çeşitkenar(x,y,z) :
    toplam = x + y + z

    return x != y != z and toplam == 180



def açı_al(x):
    açı = float(input(x + "Açıyı Girin :\n"))
    return açı

açı1 = açı_al("1. ")
açı2 = açı_al("2." )
açı3 = açı_al("3." )

eşkenar1 = eşkenar(açı1,açı2,açı3)
İkizkenar1 = İkizkenar(açı1,açı2,açı3)
çeşitkenar1 = çeşitkenar(açı1,açı2,açı3)

if eşkenar1 :
    print("Bu Bir Eşkenar Üçgendir")

elif İkizkenar1 :
    print("Bu Bir İkizkenar Üçgendir")

elif çeşitkenar1 :
    print("Bu Bir Çeşitkenar Üçgendir")

else :
    print("Bu Bir Üçgen Değildir")