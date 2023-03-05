'''Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a)	Afiseaz-o
b)	Inverseaza ordinea folosind slicing si suprascrie aceasta lista
c)	Printeaza varianta actuala (inversata)
d)	Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
e)	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
'''

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
gama = note_muzicale[::-1]
print(gama)
gama.reverse()
print(gama)

#De cate ori apare ‘do’?
print(gama.count('do'))

#Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]. Gasiti 2 variante sa le uniti intr-o singura lista.
lista1 = [3, 1, 0 ,2]
lista2 = [6, 5, 4]
print(lista1 + lista2)
lista1.extend(lista2)
print(lista1)

#Sortati si afisati lista generata la ex anterior.Stergeti numarul 0 folosind o functie.Afisati iar lista
lista1.sort()
print(lista1)
lista1.remove(0)
print(lista1)

'''Folosind un if verificati lista generata la ex3 si afisati
-	Lista este goala
-	Lista nu este goala
'''
lista1 = [3, 1, 0 ,2, 6, 5, 4]
lista_goala = []
if lista1 != lista_goala:
    print('Lista nu este goala!\n')
else:
    print('Lista este goala!\n')

#Folositi o functie care sa stearga lista de la ex3
lista1.clear()
print(lista1)

#Copy paste la ex 5. Verificati inca o data.Acum ar trebui sa se afiseze ca lista e goala.

if lista1 != lista_goala:
    print('Lista nu este goala!\n')
else:
    print('Lista este goala!\n')

# Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5} Folositi o functie ca sa afisati Elevii (cheile)
dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5}
print(dict1)
print(dict1.keys())

# Printati cei 3 elevi si notele lor.  Ex: ‘Ana a luat nota {x}’  Doar nota o veti lua folosindu-va de cheie

print(f'Ana a luat nota {dict1.get("Ana")}.\n')
print(f'Gigel a luat nota {dict1.get("Gigel")}.')
print(f'Dorel a luat nota {dict1.get("Dorel")}.')

'''Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
 Printati nota dupa modificare'''

dict1["Dorel"] = "6"
print(dict1)

# Gigel se transfera din clasa. Cautati o functie care sa il stearga. Vine un coleg nou. Adaugati Ionica, cu nota 9. Printati noii elevi
dict1.pop("Gigel")
print(dict1)
dict1['Ionica'] = '9'
print(dict1)

# Set  zile_sapt =  , 'sambata', 'duminica'}.  weekend = {'sambata', 'duminica'}  Adaugati in zilele_sapt ‘luni’  Afisati zile_sapt

zile_sapt = {'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

'''Folositi un if si verificati daca 
-	Weekend este un subset al zilelor din sapt
-	Weekend nu este un subset al zilelor din sapt
'''
if weekend != zile_sapt:
    print(f'{weekend} este un subset al zilelor din saptamana.')
else:
    print(f'{weekend} nu este un subset al zilelor din saptamana.')

# Afisati diferentele dintre aceste 2 seturi. Afisati intersectia elementelor din aceste 2 seturi
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))
print(zile_sapt.intersection(weekend))