import random

arpakuutiot = int(input("Montako arpakuutiota heitetään? "))

summa = 0

for i in range(arpakuutiot):
    heitto = random.randint(1,6)
    summa += heitto

print(f"Silmälukujen summa on {summa}.")