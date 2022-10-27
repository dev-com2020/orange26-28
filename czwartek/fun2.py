a = 10


def dodaj():
    global a
    a = 1
    b = 2
    print("Wynik= ", a + b)

print("Wartość a z góry:", a)
dodaj()
print("Wartość a z góry:", a)

