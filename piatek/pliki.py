try:
    plik = open('baza.txt', "r")
    for linia in plik:
        print(linia.strip())
    plik.close()
except FileNotFoundError:
    print("Zła nazwa pliku, spróbuj ponownie...")
finally:
    for i in range(5):
        print(i + 1 * 2)
