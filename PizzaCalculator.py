# Emiel 't Lam
# 99067718
# Pizza Calculator

SmallCost = 5.99
MediumCost = 6.99
LargeCost = 7.50

print("Hello Costumer, welcome to our pizza-ordering-site")
name = input("Please enter your name: ")
adress = input(name + " what is your adress?? : ")
#Klant krijgt de vraag hoe groot de pizza moet zijn
print("""
-------------------------------
|      Prices                
|                            
| Small costs  €5.99         
| Medium costs €6.99         
| Large costs  €7.50           
|                             
-------------------------------
""")
size = input("Would you like a Small, Medium or a Large Pizza? :")
amo = int(input("How much " + size + " pizza's would you like to get? "))
# Asks for completion of purchase
input("Thanks for your order, would you like to pay now, or will you purchase when delivery arrives? : ")
input("The pizza(s) will be delivered at " + adress + " is that correct? ")
print("Thanks, "+ name + " you will receive your pizza in " + str(amo * 4) + " minutes.")
#order completed
