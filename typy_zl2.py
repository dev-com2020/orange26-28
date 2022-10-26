lista = []
lista.append("Tomek")
lista.append("Asia")
lista.append("Michał")
lista.append("Daniel")
lista.insert(1, "Darek")
lista.pop(0)
lista.remove("Asia")
print(lista)

liczby = [54, 999, 34, 22, 12.54, 876]
liczby.sort()
liczby.reverse()
lista_zapasowa = liczby.copy()
liczby.clear()
print(liczby)
lista_zapasowa[0] = 66666
print(lista_zapasowa[0:3])
print(lista_zapasowa)
krotka = tuple(lista_zapasowa)
print(krotka)
