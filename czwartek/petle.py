czy_znasz_Pythona = False
# podatek = 0.0

if czy_znasz_Pythona:
    print("Brawo!")
else:
    print("Musisz się uczyć dalej...")

print("Ja jestem poza warunkiem!")

zarobki = int(input("Proszę, wprowadź swój dochód: "))
# < > <= >= != ==

if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.35
else:
    podatek = 0.40

print(f"zapłacisz {zarobki * podatek} zł")



