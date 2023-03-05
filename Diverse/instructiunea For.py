# problema cu dalmatienii

for i in range (1,102,2) :
    print(f'Dalmatianul cu nr {i}')

  # dalmatienii din doi in doi
for i in range(2,102, 2) :
    print(f'Dalmatianul cu nr {i}')

#parcurgere lista cu for prin intermediul indexului

numere = [3,7,10, 5, 20,30]
for i in range(0, len(numere)) :
    print(f'indexul curent este {i} ') # printeaza doar indexul. Ca sa arate frumos pot pune aici intre apostrof si partea de jos din print
    print(f'Numarul este {numere[i]}') # va lua si valoarea

# instructiunea 'for each'
for numar in numere :
    print(f'Numarul curent este {numar}')

suma = 0
for numar in numere :
    print(f'Numarul curent este {numar}')
    suma = suma + numar
print(f'Suma este {suma}')

# Exercitiu: de cate ori apare cifra 3 in lista urmatoare [3, 2, 3, 5, 3, 30, 3]

lista = [3, 2, 3, 5, 3, 30, 3]
print(lista.count(3))


