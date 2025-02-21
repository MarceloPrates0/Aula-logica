import os
os.system ("clear")

var1= float(input("Insira o valor 1: "))
var2= float(input("Insira o valor 2: "))

print(f"Seu primeiro valor é {var1}")
print(f"Seu segundo valor é {var2}")

print("\nSe alterarmos os valores: ")

aux = var2
var2 = var1
var1 = aux

print(f"\nSeu primeiro valor se torna: {var1}")
print(f"Seu segundo valor se torna: {var2}")