l_adat = []
with open('adat.txt', 'r') as f:
    for line in f:
        l_adat.append(line)

once_str = ''
for s in l_adat:
    if l_adat.index(s) == 0:
        once_str += s.strip()
    else:
        once_str += ' ' + s.strip()

with open('one_line.txt', 'w') as f_w:
    f_w.write(once_str)