class Clovek:

    def __init__(self, jmeno="", prijmeni="", pohlavi="", vek=-1):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pohlavi = pohlavi
        self.vek = vek

    def __str__(self):
        return f"Clovek => Jmeno: {self.jmeno}, Prijimeni: {self.prijmeni}, Pohlavi: {self.pohlavi}, vek: {self.vek}"

    def jeMuz(self):
        if (self.pohlavi == "muz" or self.pohlavi == "muž"):
            return True
        else:
            return False
                
zaci = []
zaci.append(Clovek("sam", "bakri", "muž", 18))
zaci.append(Clovek("armin", "lyavynets", "muž", 18))
zaci.append(Clovek("david", "reschke", "muž", 19))
zaci.append(Clovek("naty", "bakri", "zena", 19))
zaci.append(Clovek("nicholas", "ras", "muž", 18))
zaci.append(Clovek("matej", "klima", "muž", 33))

for zak in zaci:
    print(zak)




