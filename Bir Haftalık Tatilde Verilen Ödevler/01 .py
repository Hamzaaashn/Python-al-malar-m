bütçe = float(input("Lütfen Bütçenizi Girin :\n"))
toplam = 0
ürün_adları = []
döngü_koşulu = True

while döngü_koşulu  :
 
 if toplam < bütçe:
   ürün_adı = input("Ürün Adını Girin ( Çıkmak İstiyorsanız q harfine Basın) :\n")
   print()
   if ürün_adı != "q":
     
     ürün_adları.append(ürün_adı)
     
     ürün_fiyatı = float(input("Girdiğiniz Ürünün Fiyatını Girin :\n"))
     print()
   
     ürün_adları.append(ürün_fiyatı)
     toplam += ürün_fiyatı

     

     print(ürün_adları,"\nKalan Bütçe :",bütçe - toplam)
     print()
     
     if bütçe < toplam :
       print()
       print("Bütçeniz Yetmiyor ! , Başka Ürün Seçin")
       print()
       bütçe += ürün_fiyatı
       ürün_adları.remove(ürün_adı)
       print(ürün_adları,"\nKalan Bütçe :",bütçe - toplam)
       
   
   if ürün_adı == "q" :
     döngü_koşulu = False

 if bütçe == toplam :
   print("Tüm Bütçeniz Tükendi , Daha Alışveriş Yapamazsınız")
   print()
   döngü_koşulu = False


bütçe -= toplam
print( "Toplam Aldığınız Ürünler Ve Fiyatları :\n" , ürün_adları , "\nGeriye Kalan Paranız :" , bütçe , "\nToplam Yaptığınız Harcama :" , toplam )
print()
print("Uygulamadan Çıkış Yapıldı \n","İYİ ALIŞVERİŞLER :)")
print()