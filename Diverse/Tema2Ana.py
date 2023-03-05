
'''if else este un flow control, controleaza cum se desfasoara codul,
reprezinta o conditie, daca aceasta e adevarata, printeaza ruleaza codul,
else (altfel) va executa un alt cod'''

# 2. Verifica si afiseaza daca x este numar natural sau nu
x = int(input('Introdu un numar!\n'))
if x >= 0 :
    print(f'Numarul {x} este natural.')
else:
    print(f'Numarul {x} nu este natural.')

# 3. Verifica si afiseaza daca y este numar pozitiv, negativ sau neutru
y = int(input('Intoduceti un numar! \n'))
if y > 0 :
    print(f'Numarul {y} este pozitiv.')
elif y < 0 :
    print(f'Numarul {y} este negativ.')
else:
    print(f'Numarul {y} este neutru.')

# 4. Verifica si afiseaza daca x este intre -2 si 13

x = float(input('Introdu un numar!\n'))
if x > -2 and x < 13:
    print(f'Numarul {x} este intre -2 si 13.')
else:
    print(f'Numarul {x} nu este intre -2 si 13.')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = float(input('Introdu pe x!\n'))
y = float(input('Introdu pe y!\n'))
if (x - y) < 5 :
    print('X - Y =', (x-y), '< 5 !')
else:
    print('X - Y are valoarea:', (x-y))

# 6. Verifica daca a NU este intre 5 si 27. (a se folosi ‘not’)
a = int(input('Introdu pe a!\n'))
if not (5 < a < 27) :
    print(f'Valoarea {a} nu este intre 5 si 27!')
else:
    print(f'Valoarea introdusa este:{a}')

'''7. x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
'''
x = int(input('Introdu pe x!\n'))
y = int(input('Introdu pe y!\n'))
if x == y :
    print(f'Numerele {x} si {y} sunt egale!')
elif x > y:
    print(f'Numarul {x} este mai mare!')
else:
    print(f'Numarul {y} este mai mare!')

'''8. X, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare
'''
x = float(input('Introdu pe x!\n'))
y = float(input('Introdu pe y!\n'))
z = float(input('Introdu pe z!\n'))
if x == y == z :
    print('Triunghiul este echilateral!')
elif x == y and x != z :
    print('Triunghiul este isoscel!')
else:
    print('Triunghiul este oarecare!')

# 9. Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu
litera = input('Scrie o litera!\n')
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u'or litera == 'ă' or litera == 'î' :
    print(f'Litera introdusa este vocala!')
else:
    print('Litera este consoana!')

'''10. Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
x = int(input('Introduceti nota elevului!\n'))
if x > 9 :
     print('Nota este A.')
elif x > 8 :
    print('Nota este B.')
elif x > 7 :
    print('Nota este C.')
elif x > 6 :
    print('Nota este D.')
elif x > 4 :
    print('Nota este E.')
else:
    print('Nota este F.')