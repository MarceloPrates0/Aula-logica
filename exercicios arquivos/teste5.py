import os
os.system("cls || clear")

def inflacao(numero):
    if numero < 100:
        inflacionar = numero * 0.1
        total = numero + inflacionar
    else:
        inflacionar = numero * 0.2
        total = numero + inflacionar
    return total

valor = float(input("Insira o um valor: "))
print(f"\nValor total de: R${(inflacao(valor))}")
