lista = ['mar', 'para', 'cirese', 'portocale']
for x in range(len(lista)):
        print(lista[x])


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini:
     if x=='Mercedes':
        print('Am gasit masina dumneavostra.')
        break
     else:
          print('Am gasit masina ' + x + '.Mai cautam.')