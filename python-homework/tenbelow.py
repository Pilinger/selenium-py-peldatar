
beolvas = True
sum = 0

while beolvas:
    num = int(input('Kérem adjon meg egy egész számot = '))
    if num < 10:
        sum += num
    else:
        print('\n' + 'A bekért 10-nél kisebb számok összege =', sum)
        beolvas = False

