class Trida:
    def __init__(self, nazev, tridni, zaci, ucebna):
        self.nazev = nazev
        self.tridni = tridni
        self.zaci = zaci
        self.ucebna = ucebna

    def __str__(self):
        zaciStr = ""
        for zak in self.zaci:
            zaciStr += str(zak)
        return f"Trida => nazev: {self.nazev}, tridni: {self.tridni}, zaci: {zaciStr}, ucebna: {self.ucebna}"
    
    def pridejZaka(self, zak):
        self.zaci.append(zak)

    def odeberZaka(self, zak):
        self.zaci.remove(zak)
