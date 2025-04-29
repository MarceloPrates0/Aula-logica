import os
os.system("cls || clear")

def pares(numeros, par):
    par = 0
    if numeros % 2 == 0:
        par += 1
par1= 0
for i in range(1 ,7):
    numero = int(input("Insira um numero: "))
    par2 = pares(numero, par1)

print(par2)
