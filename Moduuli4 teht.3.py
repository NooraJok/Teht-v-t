luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break

if luvut:
    print(f"pienin luku: {min(luvut)}")
    print(f"suurin luku: {max(luvut)}")

else:
    print("Et antanut yhtään lukua")