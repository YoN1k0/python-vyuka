class Clovek:

    def __init__(self, jmeno="", prijmeni="", pohlavi="", vek=-1):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pohlavi = pohlavi
        self.vek = vek

    def jeMuz(self):
        if (self.pohlavi == "muz" or self.pohlavi == "muž"):
            return True
        else:
            return False
                
honza = Clovek("Honza", "Novák", "muž", 20)
petr = Clovek()
petr.jmeno = "Petr"
petr.prijmeni = "Dostál"
petr.pohlavi = "muž"
petr.vek = 18
print(honza.jmeno)
print("Je muž?", honza.jeMuz())
print(petr.jmeno)
print("Je muž?", petr.jeMuz())

