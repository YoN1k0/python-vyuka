def nactiCislo():
    return int(input("zadejte cislo"))

prvniCislo = nactiCislo()
druheCislo = nactiCislo()
operace = int(input("zadejte operaci: 1 - scitani, 2 - odcitani, 3 - nasobeni, 4 - deleni"))
if(operace == 1):
    print(prvniCislo + druheCislo)
elif(operace == 2):
    print(prvniCislo - druheCislo)
elif(operace == 3):
    print(prvniCislo * druheCislo)
else:
    print(prvniCislo / druheCislo)