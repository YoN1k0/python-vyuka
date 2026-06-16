from Clovek import Clovek
from Trida import Trida

zaci = []
zaci.append(Clovek("sam", "bakri", "muž", 18))
zaci.append(Clovek("armin", "lyavynets", "muž", 18))
zaci.append(Clovek("david", "reschke", "muž", 19))
zaci.append(Clovek("naty", "bakri", "zena", 19))
zaci.append(Clovek("nicholas", "ras", "muž", 18))
zaci.append(Clovek("matej", "klima", "muž", 33))

trida3E = Trida("3E", Clovek("Jitka", "Cernochova", "zena", 29), zaci, "M5")
trida3E.pridejZaka(Clovek("Frantisek", "Habada", "Muz", 20))
print(trida3E)