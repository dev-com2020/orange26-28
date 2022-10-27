# def odejmij(a=1, b=0):
#     print("Wynik= ", a - b)

# def oblicz_vat2(cena, vat):
#     return cena * (100 + vat) / 100

odejmij = lambda a, b: a - b
wynik1 = odejmij(5, 2)
print(wynik1)

oblicz_vat = lambda cena, vat: cena * (100 + vat) / 100

vat1 = oblicz_vat(1000, 23)
print(vat1)

lista = [1, 3, 5, 7]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3, lista))}")

wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "Dorosły")
print(wiek(5))
print(wiek(15))
print(wiek(25))