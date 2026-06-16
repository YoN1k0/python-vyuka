from Clovek import Clovek
from Trida import Trida
class Skola:
    def __init__(self, nazev: str, tridni: Clovek, zaci: list[Clovek], ucebna: str):
        self.nazev = nazev
        self.tridni = tridni
        self.zaci = zaci
        self.ucebna = ucebna
reditel = Clovek("Jan", "Novak", "muz", 55)

skola = Skola("SPŠ Brno", reditel)

ucitel1 = Clovek("Petr", "Svoboda", "muz", 42)
ucitel2 = Clovek("Jana", "Dvorakova", "zena", 38)

trida1 = Trida("1.A", ucitel1, [], "A101")
trida2 = Trida("2.B", ucitel2, [], "B205")

skola.pridejTridu(trida1)
skola.pridejTridu(trida2)

print(skola)