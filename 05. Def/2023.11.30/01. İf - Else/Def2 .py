def açılar(acı) :
    x = float(input(acı + ". Açıyı Girin :\n"))
    return x
    



def toplam():
    açı1 = açılar("1")
    açı2 = açılar("2")
    açı3 = açılar("3")

    toplama =  açı1 + açı2 + açı3
    if toplama == 180:
        print("Bu Bir Üçgen")

    else :
        print("Bu Bir Üçgen Değil")


toplam()