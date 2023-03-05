# Exercitiul 1:
# Variabilele sunt zone din memorie care conțin date de diferite tipuri
from typing import List

# Exercitiul 2:declararea si initializarea variabilelor
a = 'Hello'
b = 10
c = 20.5
d = False

print(f'Variabilele sunt urmatoarele: \n string, integer, float si boolean \n {a, b, c, d}')

# Exercitiul 3: functia type verifia tipul de date asteptat

tip_variabila_a = type(a)
print('Variabila a este de tip: ', tip_variabila_a)
tip_variabila_b= type(b)
print('Variabila b este de tip: ', tip_variabila_b)
tip_variabila_c = type(c)
print('Variabila c este de tip: ', tip_variabila_c)
tip_variabila_d = type(d)
print('Variabila d este de tip: ', tip_variabila_d)

# Exercitiul 4: functia round si suprascrierea variabilei c
c = round(c)
tip_variabila_c = type(c)
print(f'Rotunjirea variabilei este: ', c, tip_variabila_c)

# Exercitiul 5: printarea celor 4 prop folosint variabilele de mai sus
print(f'Astazi va spun: ', a, '!')
print(f'Astazi am cumparat',b, 'prune.')
print(f'Pretul per kilogram a fost:', c, "lei.")
print(f'A plouat astazi.' , d)

# Exercitiul 6:
nume = input('Care este numele tau?')
prenume = input('Care este prenumele tau? Multumesc!')
nume_prenume = nume + ' ' + prenume
print(nume_prenume)
print('Numele complet are', len(nume_prenume)-1, 'caractere.')

# Exercitiul 7:
lungimea = int(input('Introduceti valoarea lungimii, va rog: '))
latimea = int(input('Introduceti valoarea latimii, va rog: '))
aria = lungimea * latimea
print(f'Aria dreptunghiului este: ', aria)

# Exercitiul 8, 9, 10: de cate ori apare cuv the in sting - alta rezolvare mai buna cred
string = 'Coral is either the stupidest animal or the smartest rock'
x = string.count('the')
print('Cuvantul THE apare de: ', x)

# inlocuim the cu THE
y = 'the'
print(y.upper())
z = string.replace('the','THE')
print(z)

#Folosiți un assert ca să verificați dacă acest string conține doar numere.
assert (string.isnumeric())


