jmeno = input("Zadejte své jméno")  # textova promenna
vek = input("Zadejte svůj věk")            
vek = int(vek)          # ciselna promenna
bratr = input("Zadejte, zda máte bratra (True/False)")       # logicka promenna
bratr = bool(bratr)
sestra = input("Zadejte, zda máte sestru (True/False)")
sestra = bool(sestra)

print(jmeno, vek, bratr, sestra)
print("Typy proměnných jsou:")
print("jmeno: ")
print(type(jmeno))
print("vek:")
print(type(vek))
print("bratr: ")
print(type(bratr))
print("sestra: ")
print(type(sestra))