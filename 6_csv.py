path = 'rozliczenie.csv'
mode = 'r'
with open(path, mode) as moj_plik:
    content = moj_plik.readlines()

print(content)

for i in range (len(content)):
    content[i] = content[i].replace('\n', '', 1)  #usuwanie znacznika konca linii \n z konca
    content[i] = content[i].split(',')

print(content)
print(content[3])
print(content[3][2])     # pierwszy index - wiersz, drugi index - kolumna
print(content[0][2])
print(content[0][2][3:-2])


#ile kobiet na macierzynskim
licznik = 0
for i in range(len(content)):
    if content[i][4] == 't' and content[i][3] == 'k':
        licznik += 1
print('Liczba kobiet na macierzynskim = ', licznik)



# DRUGA OPCJA USUNIECIA ZNACZNIKA \N LINII NA KONCU
# for i in range (len(content)):
#     content[i][4] = content[i][4].replace('\n', '', 1)

print(content)


   # string.replace('\n', '')
print('\n\n')




#przyklad replace

slowo = 'mama.tata'
# slowo = slowo.replace('a', 'A')
# print(slowo)
slowo = slowo.replace('a', 'A', 2)
print(slowo)

#przyklad split

slowo = 'mama.tata'
slowo = slowo.split('.')
print(slowo)
