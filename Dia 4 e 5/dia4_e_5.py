def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


def calculadora():
    print('Selecione a operação')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    print("---" * 10)
    opcao = input("Digite o número da operação: ")

    if opcao == '1':
        print(f'{num1} + {num2} = {adicao(num1, num2)}')
    if opcao == '2':
        print(f'{num1} - {num2} = {subtracao(num1, num2)}')
    if opcao == '3':
        print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
    if opcao == '4':
        print(f'{num1} / {num2} = {divisao(num1, num2)}')


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("---" * 10)

calculadora()
