ludzie = ['Tomek', 'Asia', 'Michał', 'Adam']
wiek = [23, 24, 23, 21]
licznik = 5

while licznik < len(ludzie):
    person = ludzie[licznik]
    age = wiek[licznik]
    print(person, age)
    licznik += 1


while True:
    print("""
        1. dodawanie
        2. odejmowanie
        3. koniec
    """)
    wybor = input("Wprowadź numer(1-3):")
    if wybor == "1":
        print("Dodajemy...")
    elif wybor == "2":
        print("odejmujemy...")
    else:
        print("Dziękujemy, do widzenia!")
        break




