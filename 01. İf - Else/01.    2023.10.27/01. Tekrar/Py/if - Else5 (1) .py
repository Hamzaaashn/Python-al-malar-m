kullanıcı_adı = "Türkiye"
şifre = "1923" 

girilen_kullanıcı = input("Kullanıcı Adını Giriniz :\n")
girilen_şifre = input("Şifreyi Giriniz :\n")

if kullanıcı_adı == girilen_kullanıcı and şifre == girilen_şifre :
    print("Giriş Başarılı")

else:
    print("Kullanıcı adı ya da şifre yanlış")