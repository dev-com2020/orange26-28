# czy_znasz_Pythona = False
# # podatek = 0.0
#
# if czy_znasz_Pythona:
#     print("Brawo!")
# else:
#     print("Musisz się uczyć dalej...")
#
# print("Ja jestem poza warunkiem!")
#
# zarobki = int(input("Proszę, wprowadź swój dochód: "))
# # < > <= >= != ==
#
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.35
# else:
#     podatek = 0.40
#
# print(f"zapłacisz {zarobki * podatek} zł")
lista_bledow = []

alert_system = 'email'
error = 'medium'
error_message = 'Stało się coś strasznego!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'critical':
        lista_bledow.append('critical')
    elif error == 'medium':
        lista_bledow.append('medium')
    else:
        lista_bledow.append('nieznany')

print(lista_bledow)

suma_zam = 247
# if suma_zam > 100:
#     rabat = 25
# else:
#     rabat = 0

rabat = 25 if suma_zam > 100 else 0

print("SUMA:", suma_zam, "RABAT:", rabat)

lista = [j for j in range(10) if j % 2 == 0]
print(lista)

lista = []
for i in range(10):
    if i % 2 == 0:
        lista.append(i)
print(lista)
