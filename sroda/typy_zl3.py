lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior = set(lista)
# lista3 = (66, 77, 99, 999, 10)
# zbior.add(lista3)
zbior.add(18)
zbior.add(18)
zbior.add(62)
zbior.pop()
print(zbior)
lista2 = list(zbior)
# print(lista2)
zbior2 = {66, 11, 44, 18, 55, 62, 999}
print(zbior2)
print(zbior | zbior2)
print(zbior & zbior2)
print(zbior - zbior2)
print(zbior.difference(zbior2))

