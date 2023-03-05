'''1. Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

a)	Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
b)	Faceti acelasi lucru cu un for each
c)	Faceti acelasi lucru cu un while
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')
i = 0
while i < len(masini) :
    print(f'Masina mea preferata este {masini[i]}')
    i = i + 1
else:
    print(f'Am terminat lista!')

'''2. In for. Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei
'''

new_masini = []
for masini in masini :
    new_masini.append(masini.upper())
print(new_masini[1:-1])

'''3. masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for x in masini:
    if x == 'Mercedes':
        print('Am gasit masina dumneavostra.')
        break
    else:
        print('Am gasit masina ' + x + '.Mai cautam.')

'''4. Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
'''
for x in masini:
    if x =='Lastun' or x == 'Trabant':
        print(masini[0:-2])
else:
        print('Va plac masinile ' + x )

'''5. Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
-	Salvati aceste masini in masini_vechi
-	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range (len(masini)):
    if(masini[i]=='Trabant') or (masini[i]=='Lastun'):
        masini_vechi.append(masini[i])
        masini[i]='Tesla'
    else:
        continue
print(masini_vechi)
print(masini)

'''6. Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
'''
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for i in pret_masini:
    if pret_masini[i] <= 15000 :
        print(i)
for i in pret_masini.items():
    print(i)
for i in pret_masini:
    if pret_masini[i] <= 15000:
        print('Pentru un buget de sub 15.000 puteti alege masina:', i)

'''7. Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''
numere=[5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i=0
for numar in numere:
    if numar==3:
        i=i+1
print(i)



'''8. Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
print(f'Suma este {s}')


'''9. Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''
n = 0
for numar in numere:
   if numar > n:
       n = numar
print(n)


'''10. Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_noi = []
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
        numere_noi.append(numere[i])
    else:
        numere_noi.append(numere[i])
print(numere_noi)