from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek: str, szybkosc: int):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, 'lecę z prędkością:', self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek="Nieznany"):
        super().__init__(gatunek, 0)

    def dziub(self):
        print("Tu", self.gatunek, "Dziubę trawę")

    def latam(self):
        print("Ja nie latam!")

    def wydajOdglos(self):
        print("kukuryku")


# ptak1 = Ptak("Orzeł", 100)
# ptak1.latam()
ptak2 = Kura()
ptak2.latam()
ptak2.dziub()
ptak2.wydajOdglos()
