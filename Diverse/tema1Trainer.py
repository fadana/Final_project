''' a. Usor (recomandat)
1. Revizualizeaza intalnirea 1 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video cu Variabile si Tipuri de date din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video cu Operatori si Flow Control din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/
'''

'''b. Usor spre Mediu (obligatoriu)
1. 
In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila '''

print ('/n 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool Valorile le alegeti voi dupa preferinte')
marca_masina = 'golf4'
an_fabricatie = 2000
consum = 5.5
este_automata = False

print('/n 3. Utilizat functia type pentru a verifica daca au tipul de date asteptat /n ')

print(f'Marca masinii e de tipul {type(marca_masina)}')
print(f'An fabricatie e de tipul {type(an_fabricatie)}')
print(f'Consum e de tipul {type(consum)}')
print(f'este_automata e de tipul {type(este_automata)}')

print('/n 4. Rotunjiti float-ul folosind functia round() si '
      'salvati aceasta modificare in aceeasi variabila (suprascriere) Verificati tipul acesteia /n')

consum = round(consum)
print(f'Consum e de tipul {type(consum)}')

print('/n5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. (rezolvati nepotrivirile de tip prin ce modalitate doriti) /n')

print(f'Marca masinii e {marca_masina}')
print(f'An fabricatie e {an_fabricatie}')
print(f'Consumul e {consum}')

print('n/ 6. citeste de la tastatura numele citeste de la tastatura prenumele afiseaza Numele complet are x caractere /n')
nume = input('Numele tau este:')
print(f'Numele meu are {len(nume)} caractere')

print(' n/ 7. citeste de la tastatura lungimea, citeste de la tastatura latimea, Afiseaza Aria dreptunghiului este: /n')
lungime = float(input('Cati cm are lungimea dreptunghiului?'))
latime = float(input('Cati cm are latimea dreptunghiului?'))
print(f'Dreptunghiul are aria de {lungime*latime} cm.')

print('/n 8.Avand stringul: Coral is either the stupidest animal or the smartest rock. afisati de cate ori apare cuvantul the /n' )
text = 'Coral is either the stupidest animal or the smartest rock.'
numar = text.count('the')
print(f'Cuvantul the apare in text de {numar} ori')

print(' n/ 9.acelasi string inlocuieste the cu THE peste tot printeaza rezultatul /n ')
text = text.replace('the', 'THE')
print(text)

print('/n 10. acelasi string de mai sus folositi un assert ca sa verificati daca acest string contine doar numere')
assert not(text.isnumeric())
# mai sus assertul e fara not, am pus ca sa fie true si sa treaca mai departe

'''c. Optionale (may need google)
11. 
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc'''
text_dimediune_impara = input('Un text de dimensiune impara')
pozitie = len(text_dimediune_impara)//2
print(text_dimediune_impara + ' are caracterul din mijloc ' + text_dimediune_impara[pozitie])

'''12.
Folosind assert, verificati daca un string este palindrom'''
text = input("Dati un text pt verificare :")
assert text == text[::-1]

print(' /n 13.folosind o singura linie de cod citeste un string de la tastatura (ex: alabala portocala) si salveaza fiecare cuvant intr-o variabila acum printeaza ambele variabile pent verificare /n ')
# taking two inputs at a time
text1, text2 = input("da un text pt separare: ").split()
print(text1)
print(text2)

print('/n 14. citeste un string de la tastatura (eg: alabala portocala)salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter=> alAbAlA portocAla /n ')
text = input("Dati un text :")
primul_caracter = text[0]
text_modificat = text[0] + text[1:-1].replace(primul_caracter,primul_caracter.capitalize()) + text[0]
print(text)
print(text_modificat)

print('/n 15.citeste un user de la tastaturaciteste o parola afiseaza Parola: pt user x este ***** si are x caractere ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corecteg: parola abc => *** parola abcd => **** /n ' )
user = input("Dati un user :")
parola = input('Dati o parola :')
parola_ascunsa = '*'*len(parola)
print(f'parola pt userul {user} este {parola_ascunsa} si are {len(parola)} caractere')
