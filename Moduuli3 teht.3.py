sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ")
arvo = int(input("Anna hemoglobiini arvosi (g/l): "))

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiini arvosi on liian alhainen.")
    elif arvo <= 175:
       print("Hemoglobiini arvosi on normaali.")
    else:
        print("Hemoglobiini arvosi on liian korkea.")

if sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiini arvosi on liian alhainen.")
    elif arvo <= 195:
        print("Hemoglobiini arvosi on normaali.")
    else:
        print("Hemoglobiini arvosi on liian korkea.")