import os
import math
os.system("cls || clear")

def delta(a, b, c):
    return (b*b) - 4*a*c
    
def bhaskara(raizDelta):
    raizDelta1 = math.sqrt(raizDelta)
    positivo = (-b + raizDelta1)/2*a 
    negativo = (-b - raizDelta1)/2*a
    return positivo, negativo

def bhaskaraUnica(raizDelta):
    raizDelta2 = math.sqrt(raizDelta)
    positivo = (-b + raizDelta2)/2*a 
    return positivo


a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

if delta(a, b, c) > 0:
    print(bhaskara(delta(a, b, c)))
elif delta(a, b, c) == 0:
    print(bhaskaraUnica(delta(a, b, c)))
else:
    print("Sem raizes.")
