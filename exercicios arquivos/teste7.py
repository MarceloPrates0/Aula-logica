import os
import time
os.system("cls || clear")

def fahrenheit(celsius):
    conversao = (celsius * 1.8) + 32
    return conversao
def celsius(fahrenheit):
    conversao = (fahrenheit - 32) / 1.8
    return conversao

print("=== CONVERSOR DE TEMPERATURA ===")

while True:
    permissao = int(input("""
Deseja inserir à priori qual escala de grau?
1 - Celsius 
2 - Fahrenheit                                                     
"""))
    match permissao:
        case 1:
            celsius1 = float(input("Insira quantos graus Celsius deseja converter para Farenheit: "))
            for i in range(1, 4):
                print(f"{i}...")
                time.sleep(1)
                os.system("cls || clear")
            print(f"{celsius1}ºC correspondem a {fahrenheit(celsius1)}ºF")
        case 2:
            fahrenheit1 = float(input("Insira quantos graus Fahrenheit deseja converter para Celsius:"))
            for i in range(1, 4):
                print(f"{i}...")
                time.sleep(1)
                os.system("cls || clear")
            print(f"{fahrenheit1}ºF correspondem a {celsius(fahrenheit1)}ºC")
        case _:
            print("Opção inválida, selecione novamente.")

    seguimento = input("Deseja prosseguir ou encerrar o programa? 'S' para prosseguir, 'N' para encerrar: ").upper()
    match seguimento:
        case "S":
            print()
        case "N":
            break