import random
dice_list = []
counter = 1
number_of_dice_rolls = int(input("Kaç Kere Zar Atmak İstiyorsun ? :\n"))

for dice in range(1,number_of_dice_rolls + 1) :
    entered_dice = random.randint(1,6)

    dice_list.append(entered_dice)

for dice_shot in dice_list :


    print(counter,". Zar Sonucu :\n",dice_shot)
    print()
    counter += 1