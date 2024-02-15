while True :
    
    girilen_şifre = input("\nLütfen 8 Karakterlik Bir Şifre Giriniz :\n")

    if len(girilen_şifre) == 8 :
        print("Şifreniz Kaydedildi")
        break

    elif len(girilen_şifre) < 8 :
        print("Şifreniz 8 Karakterden Az")

    elif len(girilen_şifre) > 8 :
        print("Şifreniz 8 Karakterden Fazla")