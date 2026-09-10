from random import randint


spela = True


class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.poäng = 0

    def kasta(self):
        return randint(1, 6)

    def vinn_runda(self):
        self.poäng += 1


spelare1 = Spelare("James")
spelare2 = Spelare("Hames")

while spela:

    resultat1 = spelare1.kasta()

    resultat2 = spelare2.kasta()

    if resultat1 > resultat2:
        spelare1.vinn_runda()
        vinst = f"{spelare1.namn} vann denna runda!"
        if spelare1.poäng == 5:
            vinst = f"{spelare1.namn} vann hela spelet!!!"
            spela = False

    elif resultat2 > resultat1:
        spelare2.vinn_runda()
        vinst = f"{spelare2.namn} vann denna runda!"
        if spelare2.poäng == 5:
            vinst = f"{spelare2.namn} vann hela spelet!!!"
            spela = False

    else:
        vinst = f"Ni rullade samma så det blev oavgjort"

    print(f"{spelare1.namn} rollar en  {resultat1}")
    print(f"{spelare2.namn} rollar en  {resultat2}")
    print("\n")
    print(f"{vinst}""\n")
    print(spelare1.poäng)
    print(f"{spelare2.poäng}" "\n")
