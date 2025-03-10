import os
os.system ("clear")

codigo = input("Insira seu código de cadastro: ")
ano = int(input("Insira o ano em que você nasceu: "))
tempo = int(input("Insira o tempo de trabalho em anos: "))

idade = 2025-ano

print(f"\nSeu código é {codigo}.")
print(f"Seu ano de nascimento é {ano}.")
print(f"Você tem {idade} anos.")

if tempo <= 1:
    print(f"Seu tempo de trabalho é {tempo} ano")
else:
    print(f"Seu tempo de trabalho são {tempo} anos.")

if idade < 65 or tempo < 30:
    print("\nNão requerer aposentadoria.")
else:
    print("\nRequerer aposentadoria.")

