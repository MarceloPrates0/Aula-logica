import os
os.system ("cls || clear")

print("===O algoritmo se encerrará quando inserir o número '0'===\n")

contador = -1
par = -1
impar = 0
par_total = 0
valor_nota = 0

while True:
    nota = float(input("Insira sua nota: "))
    contador += 1
    valor_nota += nota

    # condições

    if nota % 2 == 0:
        par_total += nota
        par += 1
    else:
        impar += 1

    # Quebra de loop

    if nota == 0:
        break


media_pares = par_total / par
media_total = valor_nota / contador
print(contador)
print(f"Você inseriu {par} número(s) par(es) e {impar} número(s) impar(es)")
print(f"A média dos valores pares: {media_pares:.2f}")
print(f"A média geral: {media_total:.2f}")


    
    
    