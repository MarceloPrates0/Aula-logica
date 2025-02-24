import os
os.system ("clear")

def calcular_media(lista_numeros):
    total = sum(lista_numeros)
    quantidade = len(lista_numeros)
    media = total / quantidade
    return media

numeros = [2, 4, 6, 8, 10]
resultado = calcular_media(numeros)
print(resultado) # Output: 6.0