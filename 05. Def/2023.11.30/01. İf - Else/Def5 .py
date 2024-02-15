kullanıcı_adı = "Türkiye"
şifre_adı = "1923"


def girilen (x):
    sayı = input(x + "Girin :\n")
    return sayı


girilen_kullanıcı_adı = girilen("Kullanıcı Adınızı ")
girilen_şifre = girilen("Şifrenizi ")



def işlem(kullanıcı , şifre):
    
    if kullanıcı == kullanıcı_adı and şifre == şifre_adı :
        
        print("Giriş Başarılı")

    else :

        print("Kullanıcı Adı Ya Da Şifre Yanlış")


işlem(girilen_kullanıcı_adı , girilen_şifre)