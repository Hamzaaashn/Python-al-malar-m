ad = input("Adınız Ve Soyadınızı Girin :\n")
maaş = float(input("Maaşınızı Girin :\n"))
yıl = float(input("Çalışma Yılınızı Girin :\n"))

if yıl <=5 :
    maaş += maaş * 0.10
    print("Sayın",ad,"Zamlı Maaşınız" , maaş )

elif yıl <= 10 :
    maaş += maaş * 0.15
    print("Sayın",ad,"Zamlı Maaşınız" , maaş )
    
else:
    maaş += maaş * 0.25 
    print("Sayın",ad,"Zamlı Maaşınız" , maaş )