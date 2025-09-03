import random

koodi3 = "".join(str(random.randint(0, 9)) for _ in range(3))

koodi4 = "".join(str(random.randint(1, 6)) for _ in range(4))

print("Kolminumeroinen koodi (0-9): ", koodi3)
print("Nelinumeroinen koodi (1-6):", koodi4)