import os
os.system("cls || clear")
pares = 0
impares = 0
for i in range(1, 6):
    numero = int(input("Insira um numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print()
print(f"Pares: {pares}")
print(f"Impares: {impares}")
    
    
        
