import os
os.system("cls || clear")

def inflacao(numero):
    if numero < 100:
        aumento = numero + (numero * 0.1)
    else:
        aumento = numero + (numero * 0.2)
    return aumento

def descontar(numero):
    if numero < 100:
        desconto = numero - (numero * 0.1)
    else:
        desconto = numero - (numero * 0.2)
    return desconto

valor = float(input("Insira um valor: "))
print(f"\nO valor total de cobrança é: R${inflacao(valor)} ")    
print(f"\nO valor total de cobrança descontado é: R${descontar(valor)} ")    

    
        