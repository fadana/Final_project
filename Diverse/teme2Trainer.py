'''. Usor (recomandat)
1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/'''

'''b. Usor spre Mediu (obligatoriu)
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int'''
import random

# 1.
# Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else

x = int(input("vreau o valoare"))
print('2.Verifica si afiseaza daca x este numar natural sau nu')
if x >= 0:
    print(f'{x} este un numar natural')
else:
    print(f'{x} nu este un numar natural')

print('3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru')
if x > 0:
    print(f'{x} este un numar pozitiv')
elif x == 0:
    print(f'{x} este un numar neutru')
else:
    print(f'{x} nu este un numar negativ')

print('4. Verifica si afiseaza daca x este intre -2 si 13')
if x in range(-2, 14):
    print('da numarul este in interval')
else:
    print('print numarul nu este in interval')

print('5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5')
y = int(input("vreau o valoare"))
if x - y < 5:
    print('valoarea e mai mica ca 5')
else:
    print('diferenta nu e mai mica ca 5')

print('6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)')

if x not in range(5, 28):
    print(f'{x} nu este in intervalul 5 27')

print('7.x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare')
if x == y:
    print('numerele sunt egale')
else:
    print(f'Maximul numerelor este {max(x, y)}')

print('8. X, y, z - laturile unui triunghi Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.')
x = float(input('latura 1 a triunghiului este'))
y = float(input('latura 2 a triunghiului este'))
z = float(input('latura 3 a triunghiului este'))

if x == y == z:
    print('triunghiul este echilateral')
elif x != y != z:
    print('triunghiul este oarecare')
else:
    print('triunghiul este isoscel')

print('9. Citeste o litera de la tastatura Verifica si afiseaza daca este vocala sau nu')
vocale = 'aeiou'
litera = input('vreau o litera')
if litera in vocale:
    print('este vocala')
else:
    print('nu este vocala')

print(
    '10.Transforma si printeaza notele din sistem romanesc in  >Peste 9 => APeste 8 => BPeste 7 => CPeste 6 => DPeste 4 => E 4 sau sub => F')
nota = int(input('nota este'))
if nota >= 9:
    print('nota este A')
elif nota >= 8:
    print('nota este B')
elif nota >= 7:
    print('nota este C')
elif nota >= 6:
    print('nota este D')
elif nota >= 4:
    print('nota este E')
else:
    print('nota este F')

# c. Optionale (may need google)

print('11.Verifica daca x are minim 4 cifre (x e int)(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)')
x = int(input("dati un  numar pt verificare lungime"))
if len(str(x)) >= 4:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

print('12.Verifica daca x are exact 6 cifre')
# se poate verica daca x > 100000 si <1000000- cel mai mic numar de 6 cifre sau
if len(str(x)) == 6:
    print(f'{x} are exact 6 cifre')
else:
    print(f'{x} nu are fix 6 cifre')

print('13.Verifica daca x este numar par sau impar (x e int)')
if x % 2 == 0:
    print(f'{x} este numar par')
else:
    print(f'{x} este numar impar')

print('14.x, y, z (int)Afiseaza care este cel mai mare dintre ele?')
if x > y and x > z:
    print(str(x) + ' este cel mai mare numar')
elif y > x and y > z:
    print(str(y) + ' este cel mai mare numar')
else:
    print(str(z) + ' este cel mai mare numar')
# sau
print(f'cel mai mare numar este {max(x, y, z)}')

print('15. X, y, z - reprezinta unghiurile unui triunghi Verifica si afiseaza daca triunghiul este valid sau nu')
unghi1 = int(input("unghiul 1 este:"))
unghi2 = int(input("unghiul 2 este:"))
unghi3 = int(input("unghiul 3 este:"))
if unghi1 > 0 and unghi2 > 0 and unghi3 > 0:
    if unghi1 + unghi2 + unghi3 == 180:
        print('Triunghiul este valid')
    else:
        print("Triunghiul nu este valid")
else:
    print('Valoarea unghiurilor trebuie sa fie pozitiva')

print("16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'cititi de la"
      " tastatura un int xafiseaza stringul fara ultimele x caractereex: daca ati ales 7 => "
      "'Coral is either the stupidest animal or the smarte'")
text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('o valoare pozitiva pt sterge stringul'))
print(text[:-x])

print('17.acelasi string declara un string nou care sa fie format din primele 5 caractere + ultimele 5')
text_nou = text[:5] + text[len(text) - 5:]
print(text_nou)

print("18."
      "acelasi string"
      "salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock"
      "(hint: este o functie care te ajuta sa faci asta)"
      "folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant"
      "output: 'Coral is either the stupidest animal or the smartest '")
text = 'Coral is either the stupidest animal or the smartest rock'
start = text.find("rock")
print(text[:start])

print("19."
      "citeste de la tastatura un string"
      "verifica daca primul si ultimul caracter sunt la fel"
      "se va folosi un assert"
      "atentie: se doreste ca programul sa fie case insensitive"
      "'apA' e acceptat")
text = input("da-mi un  text pentru ca sa verific prima si ultima litera")
assert text[0].lower() == text[-1].lower()

print("20."
      "avand stringul '0123456789'"
      "afisati doar numerele pare"
      "acum afisati doar numerele impare"
      "(hint: folositi slicing, controlati din pas)")
text = "0123456789"
lungime_text = len(text)
text_modificat = text[0: int(lungime_text): 2]
print(text_modificat)

print("21.Verificare imbarcare persoane Tineti urmatoarele date"
      "Varsta"
      "Insotit de mama"
      "Insotit de tata"
      "Pasaport"
      "Act permisiune mama"
      "Act permisiune tata"
      "Conditii de imbarcare"
      "Daca pers are varsta peste 18 ani si are pasaport"
      "Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti"
      "Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte"
      "Aici vreau sa testati codul cu toate variantele posibile"
      "Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results")

# Ex:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Etc
varsta = int(input('Introdu varsta copilului.\n'))
pasaport = input('Introdu TRUE/False daca ai pasaport!\n')

if varsta >= 18 and pasaport is True:
    print(f'Persoana are {varsta} am pasaport.Ma pot imbarca!')
elif varsta < 18:
    if pasaport is True:
        insotit_de_mama = input('Introdu TRUE/False daca merge cu MAMA!\n')
        insotit_de_tata = input('Introdu TRUE/False daca merge cu TATA!\n')
        if insotit_de_mama is True and insotit_de_tata is True:
            print(f'Persoana are {varsta} merg cu Mama si Tata. se poate imbarca.')
        elif insotit_de_mama is True and insotit_de_tata is False:
            act_permisiune_tata = input('Introdu TRUE/False daca ai Permisiune de la Tata!\n')
            if act_permisiune_tata is True:
                print(f'Persoana are {varsta} Merge cu Mama, are permisiune tata. Se poate imbarca.')
            else:
                print(
                    f'Persoana are {varsta} merge insotit de mama dar nu are permisiunea tatalui. NU se poate imbarca!')
        elif insotit_de_mama is False and insotit_de_tata is True:
            act_permisiune_mama = input('Introdu TRUE/False daca ai Permisiune de la Mama!\n')
            if act_permisiune_mama is True:
                print(f'Persoana are {varsta} Merge cu tata, are permisiune mama. Se poate imbarca.')
            else:
                print(f'Persoana are {varsta} merge insotit de tata dar nu are permisiunea mamei. NU se poate imbarca!')
        else:
            print(f'Persoana are {varsta} si are pasaport dar nu e insotit de nici un parinte. NU se poate imbarca!')
    else:
        print(f'Persoana are {varsta} nu are pasaport.NU se poate imbarca!')
else:
    print('Nu am pasaport! Nu ma pot imbarca!')

print("22. Joc ghicit zarul"
      "Cauta pe net si vezi cum se genereaza un numar random"
      "Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll"
      "Luati un nr ghicit de la utilizator"
      "Verificati si afisati daca utilizatorul a ghicit"
      "3 optiuni"
      "Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y"
      "Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y"
      "Ai ghicit. Felicitari? Ai ales x si zarul a fost y")

numar_zar = random.randint(1, 6)
numar_ghicit = int(input("Ghiciti ce numar s-a dat cu zarul"))
if numar_zar == numar_ghicit:
    print(f'Ai ghicit. Felicitari? Ai ales {numar_ghicit} si zarul a fost {numar_zar}')
else:
    if numar_zar > numar_ghicit:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit} dar a fost {numar_zar}')
    else:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit} dar a fost {numar_zar}')
