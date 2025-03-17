import os
os.system ("cls || clear")

numero = int(input("Insira um numero: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {(numero * i)}")