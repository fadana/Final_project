# Citeste de la tastatura un string de dimensiune impara, afiseaza caracterul din mijloc
a = input('Tell me your name.')
n = len(a)
print(n)
middle_char = int(n // 2) +1
while n % 2 == 1 :
      print('Middle character of the given name is: ', str(middle_char(a)))
      n = n + 1

# Folosing assert se verifica daca stingul este palindrom
masina = 'car'
end = len(masina) - 1
palindrome = [::-1]
assert masina == 'rac'
print('This is a palindrome.')
