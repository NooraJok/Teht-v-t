import random

N = int(input("Anna arvottavien pisteiden määrä: "))

n = 0

for _ in range(N):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

pi_likiarvo = 4 * n / N

print(f"Piin likiarvo {N} pisteellä: {pi_likiarvo}")
