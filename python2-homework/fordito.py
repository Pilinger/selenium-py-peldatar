# Üres lista, és kezdő számérték bekérése
l_num = []
num = int(input('Kérem adjon meg pozitív egész számokat, majd nyomjon Enter-t! (0-val kilép): '))

# 0 megadásáig számok bekérése
while num != 0:
    l_num.append(num)
    num = int(input('Kérem adjon meg pozitív egész számokat, majd nyomjon Enter-t! (0-val kilép): '))

print('A megadott pozitív egész számok fordított listája:')
print(f'{l_num[::-1]}')
