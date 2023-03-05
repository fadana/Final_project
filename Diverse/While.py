# problema: masina merge cat timp mai are inca benzina

litri_benzina = 10
while litri_benzina > 0 :
    # acceleram masina
    print ('Vrum vrum! Acceleram!')
    # trebuie sa scadem benzina pentru ca acest loop sa nu execude la infinit
    litri_benzina = litri_benzina -1
    if litri_benzina <= 3:
        print('Se aprinde beculetul rosu!Vezi ca nu mai ai atata benzina!')
    print('Stop! Masina se opreste, nu mai are benzina!')

