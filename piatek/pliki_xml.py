import xml.etree.ElementTree as et

# drzewo = et.parse('dane.xml')
# print(type(drzewo))
# root = drzewo.getroot()
#
# imie = root.find('imie')
# print(imie.text)
# print(type(imie.text))
# adres = root.find('adres')
# miasto = adres.find('miasto')
# print(miasto.text)
# korzonek = root[3][1].text
# print(korzonek)
#
# for e in root.findall('jezyki'):
#     print(e.text)

# print(root.findall('jezyki')[1].text)

# nazwisko = root.find("nazwisko")
# print(nazwisko.attrib)
# print(nazwisko.attrib['param'])
# print(et.tostring(root))

# r = et.parse('dane.xml').getroot()
# for e in r:
#     print(e.tag, e.attrib, e.text)

r = et.parse('dane.xml').getroot()
for e in r:
    print(e.tag, e.text)

r.find('nazwisko').text = "Kaniecki"
for e in r:
    print(e.tag, e.text)

r.find('nazwisko').attrib['encoding'] = 'utf-8'
for e in r:
    print(e.tag, e.text, e.attrib)

nowy = et.Element("samochód")
nowy.text = "Kia"
r.insert(0, nowy)
for e in r:
    print(e.tag, e.text, e.attrib)

del r[1]
# naz = r.find('nazwisko')
# r.remove(naz)
for e in r:
    print(e.tag, e.text, e.attrib)


r.write("dane2.xml", encoding='utf-8')
