import os
os.system("cls || clear")

# primeiro_numero = int(input("Insira o primeiro numero: "))
# segundo_numero = int(input("Insira o segundo numero: "))

# media = (primeiro_numero + segundo_numero) / 2

# print(f"Média: {media}")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma / 2
    return media

primeiro_numero = int(input("Insira o primeiro numero: "))
segundo_numero = int(input("Insira o segundo numero: "))

media = calcular_media(primeiro_numero, segundo_numero)

print(f"Média: {media}")