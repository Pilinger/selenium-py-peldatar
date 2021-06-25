with open('adat.txt', 'r') as f:
    l_adat = []
    for line in f:
        l_adat.append(line)

once_str = ''
for s in l_adat:
    if l_adat.index(s) == 0:
        once_str += s.strip()
    else:
        once_str += ' ' + s.strip()

print(once_str)