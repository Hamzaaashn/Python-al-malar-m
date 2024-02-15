import random

while True:
    bot_list = ["Taş" , "Kağıt" , "Makas" ]
    bot_option = bot_list[random.randint(0,2)]

    user_option = input("Taş , Kağıt , Makas :\n")
    print("Bilgisayarın Seçeneği :\n",bot_option)

    if user_option == bot_option  :
        print("Berabere")

    
    elif (user_option == "kağıt" or user_option == "Kağıt") and bot_option == "Taş" :
        print("Kazandınız !")

    
    elif (user_option == "Taş" or user_option == "taş") and bot_option == "Kağıt" :
        print("Kaybettiniz :(")

    elif (user_option == "Makas" or user_option == "makas") and bot_option == "Kağıt" :
        print("Kazandınız !")

    elif (user_option == "Makas" or user_option == "makas") and bot_option == "Taş" :
        print("Kaybettiniz :(")

    elif (user_option == "Taş" or user_option == "taş") and bot_option == "Makas" :
        print("Kazandınız !")

    elif (user_option == "Kağıt" or user_option == "kağıt") and bot_option == "Makas" :
        print("Kaybettiniz :(")



    question = input("Bir Daha Oynamak İster Misiniz ? (E / H) :\n")

    if question == "E" or question == "e" :
        continue

    else :
        print("Oyun Sonlandırılıyor ...")
        break