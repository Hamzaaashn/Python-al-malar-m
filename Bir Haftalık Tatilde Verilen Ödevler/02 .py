ana_yemek = {"Döner (prs)" : 220 , "Döner (drm)" : 160, "İskender" : 250, "Et Şiş (prs)" : 250 ,
            
            "Lahmacun" : 45 , "Adana (prs)" : 200 ,"Adana (drm)" : 170 , "Köfte (ekm ar.)" : 120 , "Köfte (prs)" : 200 , 
            
            "Tavuk Kanat" : 175 , "Tavuk Şiş (prs)" : 175 , "Tavuk Döner" : 100}


salata = {"Mevsim Salatası" : 30 , "Çoban Salatası" : 30 , "Cacık" : 30}

tatlı = {"Sütlaç" : 50 , "Kadayıf" : 75 , "Baklava" : 150 , "Künefe" : 150}


içecek = {"Kola" : 30 , "Fanta" : 30 , "Ayran" : 20 , "Şalgam" : 30 , "Su" : 10}

# Değişkenler #
toplam = 0
sayaç = 0
sayaç_yemek = 0
sayaç_salata = 0
sayaç_tatlı = 0
sayaç_içecek = 0

################

sipariş_verme = input("Sipariş Vermek İster misiniz ? (E/H) \n")

sayaç += 1


while sipariş_verme == "E" :
    
    kategori_seçimi = input("Lütfen Bir Kategori Seçin \n(1 : Ana Yemek) , (2 : Salata) , (3 : Tatlı) , (4 : İçecek) :\n")
    
    if kategori_seçimi == "1" :

        for isim , ücret in ana_yemek.items():
            print(isim,"=",ücret)

        print()
        ana_yemek_seçimi = input("Lütfen Bir Yemek Seçin :\n")


        if ana_yemek_seçimi == "Döner (prs)" :
            toplam += 220

        elif ana_yemek_seçimi == "Döner (drm)" :
            toplam += 160

        elif ana_yemek_seçimi == "İskender" :
            toplam += 250

        elif ana_yemek_seçimi == "Et Şiş (prs)" :
            toplam += 250

        elif ana_yemek_seçimi == "Lahmacun" :
            toplam += 45

        elif ana_yemek_seçimi == "Adana (prs)" :
            toplam += 200

        elif ana_yemek_seçimi == "Adana (drm)" :
            toplam += 170

        elif ana_yemek_seçimi == "Köfte (ekm ar.)" :
            toplam += 120

        elif ana_yemek_seçimi == "Köfte (prs)" :
            toplam += 200

        elif ana_yemek_seçimi == "Tavuk Kanat" :
            toplam += 175

        elif ana_yemek_seçimi == "Tavuk Şiş (prs)" :
            toplam += 175

        elif ana_yemek_seçimi == "Tavuk Döner" :
            toplam += 120

        sayaç_yemek += 1

            



    if kategori_seçimi == "2" : 
        for isim , ücret in salata.items():
            print(isim,"=",ücret)
            


        salata_seçimi = input("Lütfen Bir Salata Seçin :\n")
        
        if salata_seçimi == "Mevsim Salatası" :
            toplam += 30

        elif salata_seçimi == "Çoban Salatası" : 
            toplam += 30

        elif salata_seçimi == "Cacık" : 
            toplam += 30
            
        sayaç_salata += 1      



    if kategori_seçimi == "3" :
        
        for isim , ücret in tatlı.items():
            print(isim,"=",ücret)
            


        
        tatlı_seçimi = input("Lütfen Bir Tatlı Seçin :\n")

        if tatlı_seçimi == "Sütlaç" :
            toplam += 50

        elif tatlı_seçimi == "Kadayıf" : 
            toplam += 75
        
        elif tatlı_seçimi == "Baklava" : 
            toplam += 150

        elif tatlı_seçimi == "Künefe" : 
            toplam += 150

        sayaç_tatlı += 1


    if kategori_seçimi == "4" :
        
        for isim , ücret in içecek.items():
            print(isim,"=",ücret)
            


        
        içecek_seçimi = input("Lütfen Bir İçecek Seçin :\n")
        
        if içecek_seçimi == "Kola" : 
            toplam += 30

        elif içecek_seçimi == "Fanta" : 
            toplam += 30

        elif içecek_seçimi == "Ayran" : 
            toplam += 20

        elif içecek_seçimi == "Şalgam" : 
            toplam += 30

        elif içecek_seçimi == "Su" : 
            toplam += 10
        
        sayaç_içecek += 1






    sipariş_verme = input("Başka Siparişiniz Var mı ? (E/H) \n")
    sayaç = sayaç_yemek + sayaç_salata + sayaç_tatlı + sayaç_içecek

    if sipariş_verme == "H" :

        print("\nSipariş Bilgisi :\n","\nAna Yemek",sayaç_yemek,"\nSalata",sayaç_salata,"\nTatlı",sayaç_tatlı,"\nİçecek",sayaç_içecek)
        
        if sayaç >= 3 :
           
           indirim_tutarı = toplam * 0.15
           indirimli_fiyat = toplam - indirim_tutarı
           print("Tutar :" , toplam , "\nİndirimli Tutar :" , indirimli_fiyat)

        else:
            
            print("\nToplam Tutar",toplam)