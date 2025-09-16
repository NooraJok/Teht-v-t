pituus = int(input("Kerro kuhan pituus senttimetreinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen, se on {puuttuu} cm liian lyhyt.")

else:
    print("Voit pitää saaliin. Kuha on oikean pituinen")