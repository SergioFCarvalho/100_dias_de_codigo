# Faça um programa que calcula o fatorial de um número. (Python)

import time
num = int(input("Digite um número: "))

fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
    time.sleep(0.8)
    print(i, end=' ')
print('')
print(f'O fatorial do {num} é {fatorial}')
