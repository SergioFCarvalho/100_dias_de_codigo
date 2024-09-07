n1 = float(input('Insira o primeiro número: '))
op = input('Insira a operação: +, -, /, *: ')
n2 = float(input('Insira o segundo número: '))

if op == '+':
    result = n1 + n2
if op == '-':
    result = n1 - n2
if op == '/':
    result = n1/n2
if op == '*':
    result = n1*n2

print('O resultado é ', result)
