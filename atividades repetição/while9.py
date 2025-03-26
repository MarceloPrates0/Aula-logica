import os
os.system ("cls || clear")

print("===Cálculo média===")
contador = 1
nota = float(input("\nInsira uma nota: "))
valor_nota = nota
comando = input("Deseja adicionar mais uma nota? 'S' para sim, 'N' para não: ").upper()


while comando == "S":
    contador += 1
    nota = float(input("\nInsira mais uma nota: "))
    valor_nota += nota
    comando = input("Deseja adicionar mais uma nota? 'S' para sim, 'N' para não: ").upper()
    if comando == "N":
        break

media = valor_nota / contador

print(f"Sua média: {media:.2f}")





        
        
        
