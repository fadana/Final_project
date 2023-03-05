# Declaram si initializam un Dictionary

lista_goala = []
dict_gol = {}
note_elevi = {'Gigel':10, 'Costel':9, 'Ana':10}

# Adaugam elemente unui dictionar
note_elevi['Sebi'] = 7
print(note_elevi)

# Aflam elemente din dictionar
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# Actualizarea  valorilor
note_elevi['Costel'] = 10
print(note_elevi)

# Aflam dimensiunea
print(len(note_elevi))

# Stergem valori si returneaza
note_elevi.pop('Gigel')
print(' Lista noua este:', note_elevi)

# Cautam elementul pe care l-am sters si printam
print(note_elevi.get('Gigel', 'Nu mai avem acest elev in clasa!'))

# Returneaza doar cheile
print(note_elevi.keys())
note_elevi['Andrei'] = 5
print('Noua lista este:', note_elevi)




