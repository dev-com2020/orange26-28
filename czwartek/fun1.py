a = 5
b = 6


def dodaj():
    print("Wynik= ", a + b)


def odejmij(a=1, b=0):
    print("Wynik= ", a - b)


def odejmij3(a, b, c=0):
    print("Wynik= ", a - b - c)


dodaj()
odejmij(a, b)
odejmij(b=a, a=b)
odejmij3(a, b)
