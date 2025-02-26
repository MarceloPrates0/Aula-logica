import os
os.system ("clear")

numero_um= int(input("Insira um número: "))
numero_dois= int(input("Insira um número: "))

if numero_dois > 9 and numero_um > 9:
    print("Número inválido, insira somente um dígito.")  
else:
    print(f"Estes são seus número: {numero_um}, {numero_dois}") 

print("--------")
print("\n* = Multiplicação \n+ = Adição \n- = Subtração \n/ = Divisão")

operador= input("Insira o caracter ao qual fará sua operação: ")

match operador:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        resultado = "Operação inválida"

print(f"Seu resultado é: {resultado}")



