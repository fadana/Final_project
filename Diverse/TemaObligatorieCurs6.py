'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''
class cerc:
      raza = None
      culoare = None
      def __init__(self, raza, culoare):
          self.raza = raza
          self.culoare = culoare
      def descrie_cerc(self):
          print('Cercul are culoarea', self.culoare,'si raza', self.raza)
      def aria(self):
          return int(self.raza)**2*3.14
      def circumferinta(self):
          return 2*int(self.raza)*3.14
      def diametru(self):
          return 2*int(self.raza)
cerc1 = cerc('8','albastru')
print(cerc1.descrie_cerc())
cerc2 = cerc(9, 'blue')
print(cerc2.aria())
print(cerc1.circumferinta())
print(cerc1.diametru())
print(cerc1.aria())

''' 2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''
class dreptunghi:
    lungime = None
    latime = None
    culoare = None
    def __init__(self, lungime, latime, culoare):   #constructor
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descrie_dreptunghi(self):
        print('Dreptunghiul meu are lungimea', self.lungime, 'cm, latimea', self.latime, 'cm si culoarea', self.culoare)
    def aria_dreptunghi(self):
        return int(self.lungime) * int(self.latime)
    def perimetru_dreptunghi(self):
        return (int(self.latime)) * 2 + (int(self.lungime) * 2)
    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
dreptunghi1 = dreptunghi('5', '2', 'roz')
dreptunghi1.descrie_dreptunghi()
print(dreptunghi1.aria_dreptunghi())
print(dreptunghi1.perimetru_dreptunghi())
dreptunghi1.schimba_culoarea('bordo')
dreptunghi1.descrie_dreptunghi()

'''3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
class angajat:
    nume = None
    prenume = None
    salariu = None
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descrie_angajat(self):
        print('Angajatul se numeste', self.nume, self.prenume, 'si are salariul de', self.salariu, '.')
    def nume_complet(self):
        return self.nume + ' '+ self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return int(self.salariu) * 12
    def marire_salariu(self):
        return int(self.salariu) + (int((int(self.salariu) * 5)/100))
    def marire_salariu(self, procent):
        return int(self.salariu) + int((int(self.salariu)*procent/100))

angajat1 = angajat(input('Scrieti numele dvs, va rog!\n'), input('Scrieti prenumele dvs, va rog!\n'), int(input('Scrieti salariul dvs!\n')))
angajat1.descrie_angajat()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu(5))

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
class cont:
    iban = None
    titular_cont = None
    sold = None
    def __init__(self, iban, titular_cont, sold):
      self.iban = iban
      self.titular_cont = titular_cont
      self.sold = sold
    def afisare_sold(self):
        print('Titularul', self.titular_cont, 'are in contrul', self.iban, 'suma de', self.sold, 'lei.')
    def debitare_cont(self, suma):
        if self.sold >= suma:
             self.sold = int(self.sold) - int(suma)
             return self.sold
        else:
             return 'Fonduri insuficiente!'
    def creditare_sold(self, suma1):
        return int(self.sold) + int(suma1)

titular1 = cont(input('Introduceti IBANUL contului dvs\n'), input('Introduceti numele titularului contului\n'), int(input('Introduceti soldul contului.\n')))
titular1.afisare_sold()
print('Dupa debitare, soldul contului este de ', titular1.debitare_cont(20))
print('Dupa creditare, soldul contului este de ', titular1.creditare_sold(50))
print('-------------OPTIONALE---------------------')
'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
'''
class factura:
    seria = 'ITF'
    numar_factura = None
    nume_produs = None
    cantitate = None
    pret_buc = None
    def __init__(self, numar_factura, nume_produs, cantitate, pret_buc):
        self.numar_factura = numar_factura
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        return cantitate_noua
    def schimba_pretul(self, pret):
        self.pret_buc = pret * int(self.cantitate)
        return pret
    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return nume
    def genereaza_factura(self):
        print('__________________________________\n','Factura: seria|', self.seria, '| numar',self.numar_factura, '|\n', self.nume_produs, '|', self.cantitate, '|', self.pret_buc, '|')

factura1 = factura('1', 'mere', '50', '2 lei/buc')
factura1.genereaza_factura()
print(factura1.schimba_pretul(3))
print(factura1.schimba_cantitatea(20))
factura1.genereaza_factura()

'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''

