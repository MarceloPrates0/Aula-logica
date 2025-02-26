import os
os.system ("clear")

primeiro_numero = int(input("Digite um número: "))
print("\n* = Multiplicação \n+ = Adição \n- = Subtração \n/ = Divisão")
operador = input("Digite a operação que deseja: ")
segundo_numero = int(input("\nDigite um número: "))

match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = "Operação inválida"

print(f"Seu resultado é: {resultado}")