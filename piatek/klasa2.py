class Ptak:

    def __init__(self, gatunek: str, szybkosc: int):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, 'lecę z prędkością:', self.szybkosc)

    def wydajOdglos(self):
        pass


class Kura(Ptak):

    def dziub(self):
        print("Tu", self.gatunek, "Dziubę trawę")

    def latam(self):
        print("Ja nie latam!")


ptak1 = Ptak("Orzeł", 100)
ptak1.latam()
ptak2 = Kura("Kura", 100)
ptak2.latam()
ptak2.dziub()
