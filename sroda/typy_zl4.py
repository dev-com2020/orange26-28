slownik = {}
slownik["imie"] = "Tomek"
slownik["imie"] = "Andrzej"
slownik["wiek"] = 39
lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
lista2 = [44, 55, 66, 11]
slownik["liczby"] = lista
print(slownik)
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())
print(slownik['liczby'][0])
nowa = lista + lista2
print(nowa)
