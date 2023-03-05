'''
1. Funcție care să calculeze și să returneze suma a două numere
'''
def suma_a_doua_numere():
    a = int(input('Te rog sa introduci numarul a !\n'))
    b = int(input('Te rog sa introduci numarul ! \n'))
    suma = a + b
    print(f'Suma celor doua numere este:{suma}')
    return suma
suma_a_doua_numere()
'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
def functie_par_impar():
    x = int(input('Te rog sa introduci numarul a !\n'))
    if x % 2 == 0:
        print(f'{x} este numar par')
    else:
        print(f'{x} este numar impar')
functie_par_impar()

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
def numar_caractere_din_nume():
    a = input('Te rog introdu nume si prenume!\n')
    print(f'Numarul de caractere total din numele si prenumele tau este {len(a)}')

numar_caractere_din_nume()

'''
4. Funcție care returnează aria dreptunghiului
'''
def aria_dreptunghiului():
    latimea = int(input('Va rog introduceti latimea dreptunghiului! \n'))
    lungimea = int(input('Va rog sa introduceti lungimea dreptunghiului!\n'))
    aria = latimea * lungimea
    print(f'Aria dreptunghiului este: {aria}')
    return aria
aria_dreptunghiului()

'''
5. Funcție care returnează aria cercului
'''
def aria_cercului():
    constanta_pi = 3.14
    raza_cercului = int(input('Introduceti va rog, raza cercului!\n'))
    arie_cerc = constanta_pi * raza_cercului
    print(f'Aria cercului este: {arie_cerc}')

aria_cercului()

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
'''
def functie_cauta_caracter():
    string = input('Introduceti un cuvant, va rog!\n')
    variabila = True
    if 'x' in string:
        print(variabila)
    else:
        print(f'Caracterul X nu este in {string}') # sau poate puteam si cu print(f'{string.find('x')}')

functie_cauta_caracter()

'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case este y
'''
def functie_fara_return():   #nu stiu cum sa il fac sa gaseaca upper si lower dintr-un text dat
    cuvant = input('Te rog introdu un cuvant scris cu litere mari si mici!\n')
    print(f'Numarul de caractere lower este {cuvant.lower()} si numarul de caractere upper este {cuvant.upper()}')

functie_fara_return()

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''
def lista_numere():
    lista = [0, 1, 2, -1, 5, -3]
    numere_pozitive = []
    for i in range(len(lista)):
        if lista[i] >= 0:
            numere_pozitive.append(lista[i])
        print(f'Lista cu numerele pozitive este: {numere_pozitive}')

lista_numere()

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''
def functie_simpla():
    numarul_unu = int(input('Introdu primul numar\n'))
    numarul_doi = int(input('Introdu al doilea numar\n'))

    if numarul_unu > numarul_doi:
        print(f'Primul numar {numarul_unu} este mai mare decat {numarul_doi}!')
    elif numarul_unu == numarul_doi:
        print(f'Numerele sunt egale!')
    else:
        print(f'Numarul {numarul_unu} este mai mic decat {numarul_doi}!')
functie_simpla()

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
'''
def functie_set_de_numere():
    numarul_ex_10 = int(input('Introdu un numar pt ex 10. \n'))
    set_numere={1, 2, 3, 4}
    print(f'Am adaugat numarul {set_numere.add(numarul_ex_10)}')

functie_set_de_numere()