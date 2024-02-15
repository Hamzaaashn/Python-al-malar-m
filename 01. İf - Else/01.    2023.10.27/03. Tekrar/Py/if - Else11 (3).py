açı1 = float(input("Birinci Açıyı Girin :\n"))
açı2 = float(input("İkinci Açıyı Girin :\n"))
açı3 = float(input("Üçüncü Açıyı Girin :\n"))

if açı1 == açı2 == açı3 and (açı1 + açı2 + açı3 == 180) :
    print("Bu Bir Eşkenar Üçgendir")

elif açı1 == açı2 or açı1 == açı3 or açı2 == açı3 and (açı1 + açı2 + açı3 == 180) :
    print("Bu Bir İkizkenar Üçgendir")

elif açı1 != açı2 != açı3 and (açı1 + açı2 + açı3 == 180) :
    print("Bu Bir Çeşitkenar Üçgendir")

else:
    print("Bu Bir Üçgen Değildir")