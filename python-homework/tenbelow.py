
read_in = True
summary = 0

while read_in:
    num = int(input('Kérem adjon meg egy egész számot = '))
    if num < 10:
        summary += num
    else:
        print('\n' + 'A bekért 10-nél kisebb számok összege =', summary)
        read_in = False
