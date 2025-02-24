import os
os.system ("clear")

var1= float(input("Insira o primeiro número: "))
var2= float(input("Insira o segundo número: "))
var3= float(input("Insira o terceiro número: "))

maior= max(var1, var2, var3)
menor= min(var1, var2, var3)

men= int(print(f"Seu maior número é: {maior}"))
mai= int(print(f"Seu menor número é: {menor}"))

if var1 == var2 == var3:
    print("Números iguais") 