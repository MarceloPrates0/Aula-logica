import os
os.system ("cls || clear")

for i in range(100, 121, 2):
    print(f"Numeros pares: {i}")
    
    
# ou

for i in range(100, 121):
    if i % 2 == 0:
        print(i)