# Crie um programa que converte temperatura de Celsius para Fahrenheit

def celsius_p_fahrenheit(celsius):
    fahrenheint = (celsius * 9/5) + 32
    return fahrenheint


entrada = float(input("Digite a temperatura em Grau Celsius: "))

print(f"A temperatura em Grau Fahrenheit é: {
      celsius_p_fahrenheit(entrada)} °F")
