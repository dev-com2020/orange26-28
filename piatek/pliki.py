# try:
#     plik = open('baza.txt', "r")
#     for linia in plik:
#         print(linia.strip())
#     plik.close()
# except FileNotFoundError:
#     print("Zła nazwa pliku, spróbuj ponownie...")
# finally:
#     for i in range(5):
#         print(i + 1 * 2)
lista = ['Tomek', 'Michał', 'Asia']
wyniki = []

with open(r"C:\bocian\test\baza.txt", encoding='utf-8') as p:
    for linia in p:
        wyniki.append(linia.strip())

# with open("baza.txt", "a", encoding="utf-8") as p:
#     # p.write("Witaj w świecie Pythona 7 !\n")
#     for i in lista:
#         p.write(str(i)+"\n")

print(wyniki)