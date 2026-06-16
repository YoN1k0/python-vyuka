class Clovek:

    def __init__(self, jmeno: str="", prijmeni: str="", pohlavi: str="", vek: int=-1):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pohlavi = pohlavi
        self.vek = vek

    def __str__(self):
        return f"Clovek => Jmeno: {self.jmeno}, Prijimeni: {self.prijmeni}, Pohlavi: {self.pohlavi}, vek: {self.vek}"

    def jeMuz(self) -> bool:
        if (self.pohlavi == "muz" or self.pohlavi == "muž"):
            return True
        else:
            return False
                



