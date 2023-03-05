# Exercitiu: se citeste de la tastatura un numar natural n. Sa se afiseze suma primelor n numere
print('Te rog introdu un numar in vederea calcularii sumei primelor n numere. Multumesc :)')
n = int(input('n ='))
suma_gauss = (n * (n + 1)) / 2
print('Suma lui Gauss este:', suma_gauss)

# Exercitiu: realizati un program care citeste de la tastatura doua nr naturale nenule si afiseaza suma, dif, prod, catul si restul impartirii lor
print('Salut! Te rog sa introduci doua numere. Mersi.')
a = int(input('a = '))
b = int(input('b = '))
suma = a + b
print('Suma numerelor introduse de tine este: ', suma)

diferenta = a - b
print('Diferenta numerelor introduse de tine este: ', diferenta)

produsul = a * b

print('Produsul numerelor introduse de tine este: ', produsul)

catul = a // b

print('Catul numerelor introduse de tine este: ', catul)

restul_impartirii = a % b
print('Restul impartirii numerelor introduse de tine este: ', restul_impartirii)