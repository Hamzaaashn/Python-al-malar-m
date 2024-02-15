ad = input("Lütfen Adınız Ve Soyadınızı Girin :\n")
maaş = float(input("Maaşınızı Girin :\n"))
yıl = float(input("Çalışma Sürenizi Girin :\n"))

if yıl <= 5 and yıl >= 0:
    maaş += maaş * 0.10 
    print("Sayın",ad,"Zamlı Maaşınız",maaş)

elif yıl > 5 and yıl <= 10:
    maaş += maaş * 0.15
    print("Sayın",ad,"Zamlı Maaşınız",maaş)

elif yıl >= 11 :
    maaş += maaş * 0.25
    print("Sayın",ad,"Zamlı Maaşınız",maaş)

elif yıl < 0 :
    print("Geçerli Bir Çalışma Süresi Girin")
