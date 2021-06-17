age = int(input('Kérem adja meg az életkorát egész évben = '))
drink = input('Milyen italt kér? = ')

if not(drink == 'sör' or drink == 'kóla'):
    print('Csak sör-t és kóla-t tudunk adni.')
elif age < 18 and drink == 'sör':
    print('Sajnos kiskorúnak nem adhatok sört.')
elif age >= 60 and drink == 'kóla':
    print('A koffein megemelheti a vérnyomását.')
else:
    print('Parancsoljon a', drink + '.')