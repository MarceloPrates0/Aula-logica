import os
os.system("cls || clear")

print("===Conversor de temperaturas===")
permissao = int(input("Deseja coverter qual tipo de temperatura? '1' para Fahrenheit, '2' para Celsius: "))

if permissao == 1:
    fahrenheit = float(input("Insira o grau Fahrenheit para conversão: "))
    conversao_para_celsius = (fahrenheit - 32) / 1.8
    print(f"Você inseriu {fahrenheit}°F, convertido fica {conversao_para_celsius}ºC.")
elif permissao == 2:
    celsius = float(input("Insira o grau Celsiu para conversão: "))
    conversao_para_fahrenheit = (celsius * 1.8) + 32
    print(f"Você inseriu {celsius}°C, convertido fica {conversao_para_fahrenheit}ºF.")
else:
    print("Opção inválida")