from Clovek import Clovek
class Trida:
    def __init__(self, nazev: str, tridni: Clovek, zaci: list[Clovek], ucebna: str):
        self.nazev = nazev
        self.tridni = tridni
        self.zaci = zaci
        self.ucebna = ucebna

    def __str__(self):
        zaciStr = ""
        for zak in self.zaci:
            zaciStr += str(zak) + "\n"
        return f"Trida => nazev: {self.nazev}, tridni: {self.tridni}, zaci: {zaciStr}, ucebna: {self.ucebna}"
    
    def pridejZaka(self, zak: Clovek) -> None:
        self.zaci.append(zak)

    def odeberZaka(self, zak: Clovek) -> None:
        self.zaci.remove(zak)
