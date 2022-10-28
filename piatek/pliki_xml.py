import xml.etree.ElementTree as et

drzewo = et.parse('dane.xml')
# print(type(drzewo))
root = drzewo.getroot()

imie = root.find('imie')
# print(imie.text)
# print(type(imie.text))
adres = root.find('adres')
miasto = adres.find('miasto')
# print(miasto.text)
korzonek = root[3][1].text
print(korzonek)
