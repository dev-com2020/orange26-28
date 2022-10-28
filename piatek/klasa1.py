class Dom:
    # pola klasy
    metraz = 0
    kolor = ""
    ilosc_okien = 0

    def okresl_metraz(self):
        wybor = int(input("Podaj metraż "))
        self.metraz = wybor
        print("Metraż wynosi: ", self.metraz)

    def okresl_kolor(self):
        wybor = input("Podaj kolor ")
        self.kolor = wybor
        print("Kolor wynosi: ", self.kolor)

    def okresl_okna(self):
        wybor = int(input("Podaj ilość okien "))
        self.ilosc_okien = wybor
        print("Ilość okien wynosi: ", self.ilosc_okien)
