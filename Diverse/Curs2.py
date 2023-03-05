# Operatori de atribuire
x = 10
x += 5 # x = x +5
x -= 7 # x = x-7
x *= 2 #x = x *2
x /= 3
x %= 4 # returneaza restul impartirii
x //= 2 # x la puterea a doua

# Operatori aritmetici

a = 5
b = 2
z = a ** b
print(z)

# operatori de comparare

# x == y #egal
# x != y # diferit
#x > y # mai mare
# x >= y #mai mare sau egal

# operatori logici
#x and y # si
#x or y # ori
#not x # negatie

# if statement
a = 20
b = 30
if b > a and b == a:   # uneori este nevoie de paranteze cand avem expresii de genul (b+a)
    print('succes')
#if else statement
a = 20
b = 30
if (b + a)== 58 and b > a:
    print('succes')
else:
    print('mai incearca')

# if elseif statement

a = 5
b = 9
if b < a:
    print('succes')
elif b > a:
    print('aici e bine')
elif a > b
    c = a + b
    print(type(c))
else:
    print("iesire")

# if oneline
if a > b: print('one line')

# if else in oneline
print(a) if a > b else print('b')

print(a) if a > b print('aici') elif b == a else print('b')

# nested if
if a > b:
    if a+b == 14 :
        print('succes 3')
    else:
        print('iesire 1')
else:
    print('iesire2')

# pass statement
if a < b:
    pass
elif b ** a :
    print(a)
else:
    print(b)

text = ' Coral is either the supidest animal or the smartest rock'
x = slice(5)
print(text[x]) # da primele cinci caractere - asta face sliceul, printeaza primele 5 caractere


