zbior = "Tomek", "Michał", "Asia", "Daniel"
zbior2 = "Tomek",
zbior3 = 43, 55, 22.43, 11, "Tomek", 65, 55



print(type(zbior))
print(type(zbior2))
print(zbior)
print(zbior2)
print(zbior2.count("Tomek"))
print(zbior3.count(55))
print(zbior.index("Asia"))
asia = zbior[2]
print(asia)
print(11 in zbior3)

*imie1, imie2, imie3 = zbior
print(imie1)
print(imie2)
print(imie3)

lista = list(zbior3)
print(lista)
