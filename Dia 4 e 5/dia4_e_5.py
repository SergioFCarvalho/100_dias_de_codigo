def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y


def calculadora():
    print('Selecione a operação')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    while True:
        print("---" * 10)
        opcao = input("Digite o número da operação: ")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("---" * 10)

        if opcao == '1':
            print(f'{num1} + {num2} = {adicao(num1, num2)}')
        elif opcao == '2':
            print(f'{num1} - {num2} = {subtracao(num1, num2)}')
        elif opcao == '3':
            print(f'{num1} * {num2} = {multiplicacao(num1, num2)}')
        elif opcao == '4':
            resultado = divisao(num1, num2)
            print(f'{num1} / {num2} = {resultado}')
        else:
            print('Opção inválida')
            continue

        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() == 'n':
            print("---" * 10)
            print("Calculadora encerrada")
            break


calculadora()
