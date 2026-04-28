 
def nacticislo():
   cislo1 = int(input("Zadejte prvni cislo: "))
   cislo2 = int(input("Zadejte druhe cislo: "))
   operace = input("Zadejte operaci (1 = +, 2 = -, 3 = *, 4 = /, o = odmocnina, m = mocnina): ")
   if operace == "1":
       print(cislo1 + cislo2)
   elif operace == "2":
       print(cislo1 - cislo2)
   elif operace == "3":
       print(cislo1 * cislo2)
   elif operace == "4":
       print(cislo1 / cislo2)
   elif operace == "o":
       print(cislo1 ** (1 / cislo2))
   elif operace == "m":
       print(cislo1 ** cislo2)
   
       
nacticislo()
 