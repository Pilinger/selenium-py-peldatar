l_adat = []
with open('adat.txt', 'r') as f:
    for line in f:
        l_adat.append(line)

with open('more_lines.txt', 'w') as f_w:
    f_w.writelines(l_adat)