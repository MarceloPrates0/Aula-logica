import os
os.system("cls || clear")

ListaDeNotas = []
for i in range(3):
    nota = float(input("Insira sua nota: "))    
    ListaDeNotas.append(nota)
    

print()    
for nota in ListaDeNotas: # ForEach
    print(nota)