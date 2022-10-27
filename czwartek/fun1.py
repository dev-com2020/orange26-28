# a = 5
# b = 6
x = 5
y = 6


def dodaj():
    print("Wynik= ", a + b)


def odejmij(a=1, b=0):
    print("Wynik= ", a - b)


def odejmij3(a, b, c=0):
    print("Wynik= ", a - b - c)


def oblicz_vat(cena, vat=23):
    wynik = cena * (100 + vat) / 100
    return wynik

def oblicz_vat2(cena, vat):
    return cena * (100 + vat) / 100

# print(oblicz_vat(1000,23))

wynik1 = oblicz_vat(1000)
wynik2 = oblicz_vat(1000, 8)
wynik3 = oblicz_vat(1000, 2)
print(wynik1)
print(wynik2)
print(wynik3)

# dodaj()
# odejmij()
# odejmij(x, y)
# odejmij(b=x, a=y)
# odejmij3(x, y)
