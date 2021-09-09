croiss = int(input("Aantal croissantjes: "))
stkbroden = int(input("Aantal stokbroden: "))
kbonnen = int(input("Aantal kortingsbonnen: "))
calculated = int(croiss * 39 + stkbroden * 278 - kbonnen * 50 )
txt = "De feestlunch kost je bij de bakker {} cent voor de {} croissantjes en de {} stokbroden als de {} kortingsbonnen nog geldig zijn!"
print(txt.format(calculated,croiss,stkbroden,kbonnen))