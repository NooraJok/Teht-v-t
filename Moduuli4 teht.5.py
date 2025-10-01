oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa! ")

    else:
        yritykset += 1
        print("Väärä tunnus tai salasana (yritys {yritykset/{max_yritykset}})")

    if yritykset == max_yritykset:
        print("Pääsy evätty! ")

