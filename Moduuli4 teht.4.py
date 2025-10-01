import random

salaisuus = random.randint(1, 10)

print("Arvaa kokonaisluku väliltä 1-10! ")

while True:
    try:
        arvaus = int(input("Anna arvauksesi: "))
    except ValueError:
        print("Syötäthän kokonaisluvun. ")
        continue

    if arvaus < salaisuus:
        print("Liian pieni arvaus. ")
    elif arvaus > salaisuus:
        print("Liian suuri arvaus. ")
    else:
        print("Oikein! Onnittelut! ")
        break
