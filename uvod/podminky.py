cisloStr = input("zadejte cislo")
cislo = int(cisloStr)
if(cislo > 0):
    print(cislo, "je kladne")
    if(cislo == 11):
        print("zadali jste moje oblibene cisloo")
elif(cislo < 0):
    print(cislo, "je zaporne")
else:
    print(cislo, "je nula")