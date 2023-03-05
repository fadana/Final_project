# Citeste de la tastatura un string de dimensiune impara, afiseaza caracterul din mijloc
a = input('Tell me your name.')
index = len(a)//2
print(a[index])

# Folosind assert se verifica daca stingul este palindrom
var = input()
inversul_var = var[::-1]
print(inversul_var)
assert var == var[::-1]
print('Este palindrom.')

'''Folosind o singura linie de cod, citeste un string de la tastatura
(ex: 'alabala portocala') si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pt verificare'''

b = input('What fruits do you like?')
x, y = b.split()
print (x,y)

'''Citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
'''
b = input('What fruits do you like?')
x, y = b.split()
z = x[0]
q = b[1:16]
print(q)
d = q.replace("a", "A")
print (f'a{d}a')

'''Citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
'''
user = input('Enter user name!\n')
password = (input('Enter password!\n'))
locked_password = '*' * len(password)
print(f'Parola pt user {user} este {locked_password}')



