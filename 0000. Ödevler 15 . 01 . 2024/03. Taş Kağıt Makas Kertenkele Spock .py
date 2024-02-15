import random

while True:
    bot_list = ["Taş" , "Kağıt" , "Makas" , "Kertenkele" , "Spock" ]
    bot_option = bot_list[random.randint(0,4)]

    user_option = input("Taş , Kağıt , Makas , Kertenkele , Spock :\n")
    print("Bilgisayarın Seçeneği :\n",bot_option)

    if user_option == bot_option :
        print("Berabere")

    
    elif (user_option == "Makas" or user_option == "makas") and bot_option == "Kağıt" :
        print("Kazandınız !")

    
    elif (user_option == "Kağıt" or user_option == "kağıt") and bot_option == "Taş" :
        print("Kazandınız !")


    elif (user_option == "Taş" or user_option == "taş") and bot_option == "Kertenkele" :
        print("Kazandınız !")


    elif (user_option == "Kertenkele" or user_option == "kertenkele") and bot_option == "Spock" :
        print("Kazandınız !")


    elif (user_option == "Spock" or user_option == "spock") and bot_option == "Makas" :
        print("Kazandınız !")


    elif (user_option == "Makas" or user_option == "makas") and bot_option == "Kertenkele" :
        print("Kazandınız !")


    elif (user_option == "Kertenkele" or user_option == "Kertenkele") and bot_option == "Kağıt" :
        print("Kazandınız !")


    elif (user_option == "Kağıt" or user_option == "kağıt") and bot_option == "Spock" :
        print("Kazandınız !")


    elif (user_option == "Spock" or user_option == "Spock") and bot_option == "Taş" :
        print("Kazandınız !")
        

    elif (user_option == "Taş" or user_option == "taş") and bot_option == "Makas" :
        print("Kazandınız !")

    else :
        print("Kaybettiniz :(")



    question = input("Bir Daha Oynamak İster Misiniz ? (E / H) :\n")

    if question == "E" or question == "e" :
        continue

    else :
        print("Oyun Sonlandırılıyor ...")
        break