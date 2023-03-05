# 11. Verifica daca x are minim 4 cifre (x e int)
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
import random

x = int(input('Introduceti un numar!\n'))
y = '4444'
print(len(y))
if len(str(x)) >= 4:
    print(f'Numarul {x} are patru cifre.')
else:
    print(f'Numarul {x} nu are minim 4 cifre.')

# 12. Verifica daca x are exact 6 cifre
x = int(input('Introduceti un numar!\n'))
y = '666666'
print(len(y))
if len(str(x)) == len(y):
    print(f'Numarul {x} are sase cifre.')
else:
    print(f'Numarul {x} nu are 6 cifre.')

# 13. Verifica daca x este numar par sau impar (x e int)
numar = int(input('Introdu un numar!\n'))
if numar % 2 == 0 :
    print (f'Numarul {numar} este par!')
else:
    print(f'Numarul {numar} nu este par')

# 14. x, y, z (int) Afiseaza care este cel mai mare dintre ele?
x = int(input('Introduceti x!\n'))
y = int(input('Introduceti y!\n'))
z = int(input('Introduceti z!\n'))
if z < x > y :
    print(f'Numarul {x} este cel mai mare!')
elif x < y > z :
    print(f' Numarul {y} este cel mai mare!')
elif x < z > y :
    print(f'Numarul {z} este cel mai mare!')
elif x == y and x > z :
    print(f'Numarul {x} este cel mai mare!')
elif y == z and x < y :
    print(f'Numarul {y} este cel mai mare!')
else:
    print(f'Numerele {x} {y} {z} sunt egale.')

# 15. X, y, z - reprezinta unghiurile unui triunghi. Verifica si afiseaza daca triunghiul este valid sau nu
latura_1 = float(input('Introduceti latura 1!\n'))
latura_2 = float(input('Introduceti latura 2!\n'))
latura_3 = float(input('Introduceti latura 3!\n'))
if (latura_1 + latura_2 + latura_3) == 180 :
    print('Triunghiul tau este valid!')
else:
    print('Triunghiul tau nu este valid!')

'''16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x. Afiseaza stringul fara ultimele x caractere.
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input(' Introduceti nr cu care vom scadea din caracterele stringului!\n'))
print(len(text))
print(f'{text[0:-x]}')

# 17. acelasi string. declara un string nou care sa fie format din primele 5 caractere + ultimele 5
# NU INTELEG ENUNTUL EXERCITIULUI!
text_modificat = text[0:6] + text[53:57]
print(text_modificat)

'''18. acelasi string. salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
'''
start_index = text.find('rock')
print(start_index)
print(f'{text[0:start_index]}')

'''19. citeste de la tastatura un string
verifica daca primul si ultimul caracter sunt la fel
se va folosi un assert
atentie: se doreste ca programul sa fie case insensitive
'apA' e acceptat
'''
#propozitie = input('Introdu un string.\n')
#assert propozitie[0] == propozitie[1:-1]

'''20. avand stringul '0123456789' afisati doar numerele pare. acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
'''
#string_2 = '0123456789'
#print((string_2[0:1:1]))  # in ppt -ul de la voi din prezentarea 1 e alta sintaxa, sau  nu am inteles eu ceea ce vreti sa spuneti, pg 15!!
#if (string_2[0:1:1]) % 2 == 0 and (string_2[1:2:1]) % 2 == 0 and (string_2[2:3:1]) % 2 == 0 and (string_2[3:4:1]) % 2 == 0:
    #print(f'{string_2[0:1:1]}, ')

# 21. Verificare imbarcare persoane. Tineti urmatoarele date:  Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
varsta = int(input('Introdu varsta copilului.\n'))
insotit_de_mama = input('Introdu TRUE/False daca merge cu MAMA!\n')
insotit_de_tata = input('Introdu TRUE/False daca merge cu TATA!\n')
pasaport = input('Introdu Introdu TRUE/False daca ai pasaport!\n')
act_permisiune_mama = input('Introdu TRUE/False daca ai Permisiune de la Mama!\n')
act_permisiune_tata = input('Introdu TRUE/False daca ai Permisiune de la Tata!\n')

if varsta >= 18 and pasaport is True :
    print(f'Persoana are {varsta} am pasaport.Ma pot imbarca!')
elif varsta < 18:
    if pasaport is True :
       if  insotit_de_mama is True and insotit_de_tata is True :
           print(f'Persoana are {varsta} merg cu Mama si Tata. se poate imbarca.')
       elif insotit_de_mama is True and act_permisiune_tata is True :
           print(f'Persoana are {varsta} Merge cu Mama, are permisiune. Se poate imbarca.')
       elif insotit_de_tata is True and act_permisiune_mama is True :
           print(f'Persoana are {varsta} merge cu TATA si are permisiune.Se poate imbarca.')
       elif insotit_de_mama is False or insotit_de_tata is False :
           print(f'Persoana are {varsta} nu merge insotit . NU se poate imbarca!')
       elif insotit_de_mama is True and act_permisiune_tata is False :
           print(f'Persoana are {varsta}  merge insotit dar nu are permisiunea parintelui. NU se poate imbarca!')
       elif insotit_de_tata is True and act_permisiune_mama is False :
           print(f'Persoana are {varsta}  merge insotit dar nu are permisiunea parintelui. NU se poate imbarca!')
    if pasaport is False :
        print(f'Persoana are {varsta} nu are pasaport.NU se poate imbarca!')
else:
      print('Nu am pasaport! Nu ma pot imbarca!')

# 22. joc de ghicit zarul
dice_roll = random.choice([1, 2, 3, 4, 5, 6])
utilizator = int(input('Ce numar alegi?\n'))

if dice_roll == utilizator :
    print('Egalitate!')
elif utilizator == 1 and utilizator < dice_roll:
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {utilizator}, iar computerul {dice_roll}')
elif utilizator == 2 and utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {utilizator}, iar computerul {dice_roll}')
elif utilizator == 3 and utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {utilizator}, iar computerul {dice_roll}')
elif utilizator == 4 and utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {utilizator}, iar computerul {dice_roll}')
elif utilizator == 5 and utilizator < dice_roll :
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales: {utilizator}, iar computerul {dice_roll}')
elif utilizator <= 6 and utilizator > dice_roll :
    print(f'Ai castigat! Ai ales un numar mai mare. Ai ales: {utilizator}, iar computerul {dice_roll}')
else:
    print(f'Introdu un nr de la 1 - 6. Ai ales: {utilizator}.')


