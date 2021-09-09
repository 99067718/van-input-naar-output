AantPers = int(input("Aantal personen: "))
AantMin = int(input("Aantal minuten VIP VR per persoon: "))
finalNumber = round(int((7.45 * AantPers) + (AantMin * 0.37 / 5) * AantPers*100),2)
txt = "Dit geweldige dagje uit met {} mensen in de speelhal met {} minuten kost je maar {} cent."

print(txt.format(AantPers,AantMin,finalNumber))