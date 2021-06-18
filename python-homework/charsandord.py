
a = ord('a')

for i in range(10):
    if i < 26 % 10:
        print(f'{chr(a + i)}', a + i, f'{chr(a + i + 10)}', a + i + 10, f'{chr(a + i + 20)}', a + i + 20)
    else:
        print(f'{chr(a + i)}', a + i, f'{chr(a + i + 10)}', a + i + 10)