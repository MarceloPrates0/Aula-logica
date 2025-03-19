import os
os.system("clear")

nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))

while True:
    if nota_1 < 0 or nota_1 > 10:
        nota_1 = float(input("Insira a primeira nota: "))
    else:  
        if nota_2 < 0 or nota_2 > 10:
            nota_2 = float(input("Insira a segunda nota: "))
        else:
            break
        
media = (nota_2 + nota_1) / 2

print(f"Sua média: {media}")
    
# Forma professor 

# QUANTIDADE_NOTAS = 2
# soma = 0

# for i in range(QUANTIDADE_NOTAS):
#     while True:
#         nota = float(input("Insira sua nota: "))

#         if nota < 0 or nota > 10:
#             print("A nota deveser entre 0 e 10.\n")
#         else:
#             soma+=nota
#             break

# media = soma / QUANTIDADE_NOTAS

# print(f"Média: {media}")