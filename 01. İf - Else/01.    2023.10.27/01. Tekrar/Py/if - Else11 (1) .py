print("Merhaba ! Üçgeninizin 3 Açısını Sisteme Girin\n")

açı1 =  float(input("1. Açıyı Girin :\n"))
açı2 =  float(input("2. Açıyı Girin :\n"))
açı3 =  float(input("3. Açıyı Girin :\n"))

if açı1 == açı2 == açı3 and (açı1 + açı2 + açı3 == 180):
    print("Bu Bir Eşkenar Üçgendir")

elif açı1 == açı2 or açı1 == açı3 or açı2 == açı3 and (açı1 + açı2 + açı3 == 180):
    print("Bu Bir İkizkenar Üçgendir")
    
elif açı1 != açı2 != açı3 and (açı1 + açı2 + açı3 == 180):
    print("Bu Bir Çeşitkenar Üçgendir")

else:
    print("Bu Bir Üçgen Değildir")