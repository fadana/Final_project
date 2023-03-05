# un text scris pe doua linii, se pun 3 apostrof la inceput si la final.

str4 = '''Un text scris
pe două linii.'''
print(str4)

# media aritmetica formula normala este cu 3 nr si cu declararea variabilelor =int(input('a='))
a_i = [10, 4,7]
print(a_i)
m =len(a_i)
media_aritmetica = sum(a_i)/m
print(media_aritmetica)

# Rasturnatul unui numar este
# prima data introducem numarul de la tastatura
# cifra unitatilor va deveni cifra zecilor definim variabile care returneaza restul impartirii la 10
# apoi trebuie sa definim o alta variabila care sa calculeze noul numar
print('Te rog introdu un numar de doua cifre ')
n = int(input('n='))
c1 = n % 10
c2 = (n // 10)
invers = c1 * 10 + c2
print('Rasturnatul numarului introdus este ', invers)

# o variabila string reprezinta un loc din memoria calculatorului care se materializeaza intr-un sir de caractere

for i in range(1,20, 3):
    print(i)