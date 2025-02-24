import os
os.system ("clear")


n1= float(input("Seu número: "))
n2= float(input("Seu número: "))
def soma(n1, n2):
    return n1 + n2%50

resultado = soma(n1, n2)
print(resultado) 