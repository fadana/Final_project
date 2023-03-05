# JaVA
# declarare si initializare array cand stim valorile
# contine mai multe elemente de acelasi tip
# are o dimensiune fixa, proprietarea length care ne da dimensiunea array-ului
# accesam elementele prin index, care incepe de la 0

# listele in python pot sa cuprinda elemente de tipuri diferite si au dimensiune dinamica

fructe = ['mar', 'banana', 'portocala', 3, True]    # ar trebui paranteze drepte
print(fructe)

# accesam un element in functie de index

print(fructe[1])                  # paranteze drepte dupa fructe

# adaugarea unui nou element
fructe.append('rosie')
 
#suprascriem un element
fructe[0] = 'para'               #paranteze drepte dupa fructe
print(fructe)

 # aflam dimensiunea unei liste
print(len(fructe))

# scoate si ne returneaza ultimul element al listei
last = fructe.pop()
print('Ultimul element al listei este:', last)
print('Noua lista dupa ce am scos rosie este: ', fructe)

# de cate ori apare un element?

fructe_nou = ['mar', 'banana', 'portocala', 3, True, 3]
print(fructe_nou.count(3))


fructe_exotice = ['ananas', 'kiwi']
fructe_exotice.append('avocado')
print('Lista dupa ce am adaugat este:', fructe_exotice)

# extinderea listei initiale se face cu functia append

fructe.extend(fructe_exotice)
print('Lista dupa ce am extins-o cu fructe exotice este: ', fructe)







