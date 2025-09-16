leiviskat = int(input("Anna leivistkät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luodit_yht = leiviskat * 20 * 32 + naulat * 32
grammat = luodit_yht * 13.3

kilot = int(grammat // 1000)
loput_grammat = grammat % 1000

print(f"Massa nykymittojen mukaan: {kilot} kg ja {loput_grammat:.2f} g")