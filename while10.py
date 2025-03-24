import os
os.system ("cls | clear")

contador = 1
nota = float(input("Insira sua nota: "))
valor_nota = nota

while nota > 0:
    nota = float(input("Insira mais uma nota: "))
    if nota > 0:
        valor_nota += nota
        contador += 1
    if nota < 0:
        break

media = valor_nota / contador
print(f"Sua média: {media}")